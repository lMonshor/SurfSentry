import socket
import os
import time
import requests
import psutil
import json
import threading
from scapy.layers.inet import IP
from scapy.all import sniff
from PyQt5.QtCore import (
    QMetaObject, Qt, Q_ARG, pyqtSignal, pyqtSlot,
    QCoreApplication, QEvent
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (
    QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QVBoxLayout, QWidget, QMessageBox
)


class MaliciousIpDownloader:
    def __init__(self, domain_file, ip_file, output_file):
        self.domain_file = domain_file
        self.ip_file = ip_file
        self.output_file = output_file
        self.merged_data = []
        self.total_pages = 5

    def get_malicious_data(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        for i in range(1, self.total_pages + 1):
            url = f"https://www.usom.gov.tr/api/address/index?page={i}"
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    self.merged_data.append(data)
                    loading_screen.update_label(
                        f"Data from page {i} successfully retrieved.")
                else:
                    loading_screen.update_label(
                        f"Request failed. {response.status_code}")
            except requests.exceptions.RequestException:
                loading_screen.update_label(
                    f"Request error: Page {i} data unretrieved ConnectionTimeOut")
                continue
        loading_screen.update_label("Data is being processed...")
        with open(self.output_file, "w", encoding="utf-8") as file:
            json.dump(self.merged_data, file, ensure_ascii=False)

    def parse_resolve(self):
        urls_count = 0
        with open(self.domain_file, "w", encoding="utf-8") as f, open(self.ip_file, "w") as g:
            with open(self.output_file, "r", encoding="utf-8") as file:
                data = json.load(file)
            for page in data:
                for model in page["models"]:
                    url = model["url"]
                    desc = model["desc"]
                    criticality_level = model["criticality_level"]
                    try:
                        ip = socket.gethostbyname(url)
                        g.write(ip + "\n")
                        f.write(f"URL: {url}\n")
                        f.write(f"IP: {ip}\n")
                        if desc == "BP":
                            f.write("Title: Financial Phishing\n")
                            f.write("Desc: Finsans sektörüne özel olarak gerçekleştirilen sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.\n")
                        elif desc == "PH":
                            f.write("Title: Phishing\n")
                            f.write(
                                "Desc: Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.\n")
                        elif desc == "MD":
                            f.write("Title: Malware Distribution Domain\n")
                            f.write(
                                "Desc: Zararlı yazılımların çalışması için bir bölümünün veya tamamının indirildiği alan adlarına ait kategoridir.\n")
                        f.write(f"Criticality Level: {criticality_level}\n")
                        f.write("\n")
                        urls_count += 1
                    except socket.gaierror:
                        pass
        return urls_count

    def run(self):
        loading_screen.update_label(
            "Searching For Malicious Datas from USOM \n Please Wait...")
        time.sleep(2)
        self.get_malicious_data()
        self.urls_count = self.parse_resolve()


class NetworkTrafficMonitor:

    def __init__(self, window, ip_list_file):
        self.window = window
        self.malicious_ips = set()
        self.warning_shown = set()
        self.load_malicious_ips(ip_list_file)
        self.domain_info = self.parse_domain_info("Datas/domain-list.txt")

    def is_running(self):
        return self.running

    def load_malicious_ips(self, ip_list_file):
        with open(ip_list_file, "r") as f:
            self.malicious_ips = {ip.strip() for ip in f}

    def parse_domain_info(self, file_path):
        domain_info = {}
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.read().split('\n\n')
            for block in lines:
                lines_in_block = block.split('\n')
                target_ip = None
                for line in lines_in_block:
                    if line.startswith('IP: '):
                        target_ip = line.split('IP: ')[1]
                        break
                if target_ip:
                    domain_info[target_ip] = {}
                    for line in lines_in_block:
                        if line.startswith('URL:'):
                            domain_info[target_ip]['URL'] = line.split('URL: ')[
                                1]
                        elif line.startswith('IP:'):
                            domain_info[target_ip]['IP'] = line.split('IP: ')[
                                1]
                        elif line.startswith('Title:'):
                            domain_info[target_ip]['Title'] = line.split('Title: ')[
                                1]
                        elif line.startswith('Desc:'):
                            domain_info[target_ip]['Desc'] = line.split('Desc: ')[
                                1]
                        elif line.startswith('Criticality Level:'):
                            domain_info[target_ip]['Criticality Level'] = int(
                                line.split('Criticality Level: ')[1])
        return domain_info

    def packet_callback(self, packet):
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            if ip_src in self.malicious_ips or ip_dst in self.malicious_ips:
                matched_domains = self.domain_info.get(ip_dst)
                if matched_domains:
                    message = f"Caution: You are communicating with a malicious IP address!\n\nURL: {matched_domains.get('URL')}\nIP: {matched_domains.get('IP')}\nTitle: {matched_domains.get('Title')}\nDesc: {matched_domains.get('Desc')}\nCriticality Level: {matched_domains.get('Criticality Level')}"
                    if message not in self.warning_shown:
                        self.warning_shown.add(message)
                        QMetaObject.invokeMethod(
                            self.window, "show_warning_signal", Qt.QueuedConnection,
                            Q_ARG(str, "Warning"),
                            Q_ARG(str, message))

    def start_sniffing(self):
        self.running = True
        sniff_thread = threading.Thread(target=self.sniff_packets)
        sniff_thread.start()
        main_window.readonly_label.setText("Status: Sniffing started.")

    def stop_sniffing(self):
        self.running = False
        main_window.readonly_label.setText(
            "Status: Ready for sniffing, please start analysis.")

    def sniff_packets(self):
        sniff(iface=main_window.current_adapter, prn=self.packet_callback,
              stop_filter=lambda _: not self.running, store=0)


class LoadingScreenDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle('Updating Malicious Data')

        layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.ok_button = QPushButton("OK")
        self.ok_button.setEnabled(False)
        self.ok_button.clicked.connect(self.close)

        layout.addWidget(self.ok_button)

        self.setModal(True)
        self.show()

    def start_loading(self):
        self.exec_()

    def update_label(self, text):
        self.label.setText(text)

    def update_ok_button(self, completed):
        if completed:
            self.ok_button.setEnabled(completed)


class MainWindow(QWidget):
    show_warning_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon("Assets/icon.png"))
        self.show_warning_signal.connect(self.show_warning)

    def initUI(self):
        self.setWindowTitle('SurfSentry')
        self.setFixedSize(400, 550)
        self.current_adapter = self.get_current_adapter()

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        malicious_domains_label = QLabel('Malicious Datas:')
        malicious_domains_label.setFont(QFont("Arial", 10, QFont.Bold))
        main_layout.addWidget(malicious_domains_label)

        self.plain_text = QPlainTextEdit()
        self.plain_text.setReadOnly(True)
        main_layout.addWidget(self.plain_text)

        button_layout = QVBoxLayout()
        button_layout.setContentsMargins(10, 20, 10, 10)

        self.update_ip_list_button = QPushButton('Update Data')
        self.update_ip_list_button.clicked.connect(self.update_ip_list)
        button_layout.addWidget(self.update_ip_list_button)

        self.start_analysis_button = QPushButton('Start Analysis')
        self.start_analysis_button.setEnabled(False)
        self.start_analysis_button.clicked.connect(self.start_analysis)
        button_layout.addWidget(self.start_analysis_button)

        self.stop_analysis_button = QPushButton('Stop Analysis')
        self.stop_analysis_button.setEnabled(False)
        self.stop_analysis_button.clicked.connect(self.stop_analysis)
        button_layout.addWidget(self.stop_analysis_button)

        main_layout.addLayout(button_layout)

        self.readonly_label = QLabel()
        self.readonly_label.setAlignment(Qt.AlignLeft)
        self.readonly_label.setWordWrap(True)
        self.readonly_label.setText("Status: Please update malicious data.")
        self.readonly_label.setStyleSheet("background-color: lightgray;")
        main_layout.addWidget(self.readonly_label)

        self.readonly_label2 = QLabel()
        self.readonly_label2.setAlignment(Qt.AlignLeft)
        self.readonly_label2.setWordWrap(True)
        self.readonly_label2.setText(f"Active Adapter: {self.current_adapter}")
        self.readonly_label2.setStyleSheet("background-color: lightgray;")
        main_layout.addWidget(self.readonly_label2)

        self.show()

    def get_network_adapters(self):
        adapters = []
        for iface, nic_data in psutil.net_if_addrs().items():
            for addr in nic_data:
                if addr.family == socket.AF_INET:
                    adapters.append(iface)
                    break
        return adapters
    
    def get_current_adapter(self):
        active_ip = socket.gethostbyname(socket.gethostname())
        adapters = self.get_network_adapters()
        for adapter in adapters:
            iface = psutil.net_if_addrs()[adapter]
            for nic in iface:
                if nic.family == socket.AF_INET and nic.address == active_ip:
                    return adapter
        
        return None

    def download_update_ip_list(self, downloader, loading_screen):
        downloader.run()
        loading_screen.update_ok_button(True)
        loading_screen.update_label(
            f'Done! \n {downloader.urls_count} Malicious data updated.')
        main_window.readonly_label.setText(
            "Ready for sniffing, please start analysis.")
        self.start_analysis_button.setEnabled(True)
        

    def update_ip_list(self):
        downloader = MaliciousIpDownloader(
            "Datas/domain-list.txt", "Datas/ip-list.txt", "Datas/data.json")

        downloader_thread = threading.Thread(
            target=self.download_update_ip_list, args=(downloader, loading_screen))
        downloader_thread.start()

        loading_screen.start_loading()
        self.load_domain_list()

    def load_domain_list(self):
        self.plain_text.clear()
        with open("Datas/domain-list.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            numbered_list = []
            count = 1
            for line in lines:
                line = line.strip()
                if line.startswith("URL:"):
                    url = line.split(":")[1].strip()
                    numbered_list.append(f"{count} - URL: {url}")
                elif line.startswith("IP:"):
                    ip = line.split(":")[1].strip()
                    numbered_list.append(f"    IP: {ip}")
                elif line.startswith("Title:"):
                    title = line.split(":")[1].strip()
                    numbered_list.append(f"    Title: {title}")
                elif line.startswith("Desc:"):
                    desc = line.split(":")[1].strip()
                    numbered_list.append(f"    Desc: {desc}")
                elif line.startswith("Criticality Level:"):
                    level = line.split(":")[1].strip()
                    numbered_list.append(f"    Criticality Level: {level} \n")
                    count += 1
            self.plain_text.setPlainText("\n".join(numbered_list))

    def start_analysis(self):
        self.monitor = NetworkTrafficMonitor(self, "Datas/ip-list.txt")
        self.monitor.start_sniffing()
        self.start_analysis_button.setEnabled(False)
        self.stop_analysis_button.setEnabled(True)
        self.update_ip_list_button.setEnabled(False)

    def stop_analysis(self):
        self.monitor.stop_sniffing()
        self.start_analysis_button.setEnabled(True)
        self.stop_analysis_button.setEnabled(False)
        self.update_ip_list_button.setEnabled(True)

    def closeEvent(self, event):
        try:
            if self.monitor and self.monitor.is_running():
                self.monitor.stop_sniffing()
            QCoreApplication.quit()
        except:
            pass

    @pyqtSlot(str, str)
    def show_warning(self, title, text):
        QMessageBox.warning(self, title, text)


if __name__ == "__main__":
    app = QApplication([])
    icon_path = os.path.abspath("Assets/icon.png")
    app.setWindowIcon(QIcon(icon_path))
    main_window = MainWindow()
    main_window.show()
    loading_screen = LoadingScreenDialog()
    loading_screen.hide()
    app.exec_()
