import socket
import subprocess
from datetime import datetime

def filter_raw_data_item(item):
    try:
        if item['type'] == 'domain' or item['type'] == 'ip':
            if item['type'] == 'ip':
                ip = item['url']
            if item['type'] == 'domain':
                ip = resolve_domain(item['url'])
            if ip is not None:
                return {
                    'data_id': item['id'],
                    'data_type': item['type'],
                    'url': item['url'],
                    'resolved_ip': ip,
                    'type': (
                        'Phishing'
                        if item['desc'] == 'PH' else
                        'Financial Phishing'
                        if item['desc'] == 'BP' else
                        'Malware Distribution Domain'
                        if item['desc'] == 'MD' else
                        'Malware Distribution IP'
                        if item['desc'] == 'MI' else
                        'Malware Distribution URL'
                        if item['desc'] == 'MU' else
                        'Malware Command Center'
                        if item['desc'] == 'MC' else
                        'Cyber Attack (Port Scan, Brute Force etc.)'
                        if item['desc'] == 'CA' else
                        'Not available'
                    ),
                    'desc': (
                        'The category containing malicious domain names, IP addresses, or links targeting social engineering attacks outside the finance sector.'
                        if item['desc'] == 'PH' else
                        'It is the category that contains malicious domain names, IP addresses, or links specifically targeting the finance sector with social engineering attacks.'
                        if item['desc'] == 'BP' else
                        'It is the category related to domain names where a portion or all of the malicious software is downloaded for execution.'
                        if item['desc'] == 'MD' else
                        'It is the category related to IP addresses from which a portion or all of the malicious software is downloaded for execution.'
                        if item['desc'] == 'MI' else
                        'It is the category related to links from which a portion or all of the malicious software is downloaded for execution.'
                        if item['desc'] == 'MU' else
                        'It is the category containing domain names, IP addresses, or links used for malicious activities.'
                        if item['desc'] == 'MC' else
                        'It is the category that regularly contains domain names, IP addresses, or links engaged in malicious activities.'
                        if item['desc'] == 'CA' else
                        'Not available'
                    ),
                    'criticality_level': item['criticality_level'],
                    'source': (
                        'USOM'
                        if item['source'] == 'US' else
                        'CERT'
                        if item['source'] == 'SO' else
                        'RSA'
                        if item['source'] == 'RS' else
                        'REPORTING'
                        if item['source'] == 'IH' else
                        'Not available'
                    ),
                    "date": item['date'].split()[0],
                    'link': f"https://www.usom.gov.tr/adres/{item['id']}"
                }
    except Exception as e:
        print(f"An error occured: {e}")
    return None


def process_malicious_data(raw_data):
    filtered_data = {'items': []}
    for item in raw_data:
        filtered_item = filter_raw_data_item(item)
        if filtered_item:
            filtered_data['items'].append(filtered_item)
    return filtered_data


def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        print(f"unresolved: {domain}")
        return None


def flush_dns():
    command = f"powershell ipconfig /flushdns"
    subprocess.run(command, shell=True)

def get_current_date_utc():
    return str(datetime.now().utcnow())

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")