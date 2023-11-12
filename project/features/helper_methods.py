import subprocess
import psutil
import socket
from datetime import datetime, timedelta
from PyQt6 import QtCore, QtGui
import smtplib
from email.mime.text import MIMEText
import config


def flush_dns():
    try:
        command = f"powershell ipconfig /flushdns"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error flush_dns: {e}")


def get_current_date_utc():
    return str(datetime.now().utcnow())


def get_previous_date_utc():
    today = datetime.now().utcnow()
    previous_date = today - timedelta(days=2)
    return str(previous_date)


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def open_custom_page(link):
    try:
        url = QtCore.QUrl(link)
        QtGui.QDesktopServices.openUrl(url)
    except Exception as e:
        print(f"Error openCustomWebPage: {e}")


def send_email_feedback(email_address, subject, description):
    try:
        sender = config.email
        receiver = config.receiver_email
        password = config.password

        message = (f"Email Address: {email_address.toPlainText()}\nSubject: {subject.toPlainText()}\nDescription: {description.toPlainText()}")

        msg = MIMEText(message)
        msg['Subject'] = "Feedback"
        msg['From'] = sender
        msg['To'] = receiver

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, receiver, msg.as_string())

        email_address.clear()
        subject.clear()
        description.clear()

        print("Message sent!")

    except Exception as e:
        print(f"An error occurred: {e}")


def get_network_adapters():
    adapters = []
    for iface, nic_data in psutil.net_if_addrs().items():
        for addr in nic_data:
            if addr.family == socket.AF_INET:
                adapters.append(iface)
                break
    return adapters


def get_current_adapter():
    active_ip = socket.gethostbyname(socket.gethostname())
    adapters = get_network_adapters()
    for adapter in adapters:
        iface = psutil.net_if_addrs()[adapter]
        for nic in iface:
            if nic.family == socket.AF_INET and nic.address == active_ip:
                return adapter

    return None
