from db import db_operations
from features import helper_methods


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
                "date": item['date'],
                'link': f"https://www.usom.gov.tr/adres/{item['id']}"
            }
    except Exception as e:
        print(f"Error filter_mal_raw_data_item: {e}")
    return None


def fill_mal_data_table(raw_mal_data):
    for raw_mal_data_item in raw_mal_data:
        filtered_item = filter_mal_raw_data_item(raw_mal_data_item)
        if filtered_item:
            if not check_mal_data_existence(filtered_item=filtered_item):
                db_operations.save_to_mal_table(filtered_item)
                fill_blocked_data_table()


def fill_blocked_data_table():
    mal_data = db_operations.custom_query('select * from malicious_data')
    if mal_data:
        for item in mal_data:
            if not check_blocked_data_existence(item):
                operation_time = helper_methods.get_current_date()
                db_operations.save_to_blocked_table(
                    item=item, op_time=operation_time)


def check_blocked_data_existence(item):
    data = db_operations.custom_query(
        f'select * from blocked_data where url = "{item[3]}"')
    if data:
        # Exist
        return True
    else:
        return False


def check_mal_data_existence(filtered_item):
    data = db_operations.custom_query(
        f'select * from malicious_data where url = "{filtered_item['url']}"')
    if data:
        # Exist
        return True
    else:
        return False


def clear_old_data_from_mal_data():
    today = helper_methods.get_current_date_utc().split()[0]
    data = db_operations.custom_query(
        "select data_id,date from malicious_data")
    if data:
        for item in data:
            item_data_id = item[0]
            item_date = item[1]
            if item_date.split()[0] != today:
                db_operations.custom_query(
                    f'delete from malicious_data where data_id = "{item_data_id}"')


def get_last_mal_data_date():
    last_data_date = db_operations.custom_query(
        "select date from malicious_data order by data_id desc limit 1")
    if last_data_date:
        return last_data_date[0][0]
    else:
        return None
