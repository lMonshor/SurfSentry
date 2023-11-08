import subprocess
from datetime import datetime
from db import db_operations
from datetime import datetime, timedelta


def filter_mal_raw_data_item(item):
    try:
        if item['type'] == 'domain' or item['type'] == 'ip':
            return {
                'data_id': item['id'],
                'data_type': item['type'],
                'url': item['url'],
                'mal_type': (
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
        print(f"Error filter_mal_raw_data_item: {e}")
    return None


def process_malicious_data(raw_mal_data):
    db_operations.create_tables()
    db_operations.clear_table_by_table_name('malicious_data')
    for item in raw_mal_data:
        filtered_item = filter_mal_raw_data_item(item)
        if filtered_item:
            db_operations.save_to_mal_table(filtered_item)
            operation_time = get_current_date()
            if not check_blocked_data_existence(filtered_item):
                db_operations.save_to_blocked_table(
                    item=filtered_item, op_time=operation_time)


def check_blocked_data_existence(filtered_item):
    data = db_operations.custom_query(
        f'select * from blocked_data where url = "{filtered_item['url']}"')
    if data:
        # Exist
        return True
    else:
        return False


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
    previous_date = today - timedelta(days=1)
    return str(previous_date)


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")
