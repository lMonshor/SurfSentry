from db import db_operations
from features import helper_methods


def filter_raw_entry(raw_entry, update_date):
    try:
        type_mapping = {
            'PH': 'Phishing',
            'BP': 'Financial Phishing',
            'MD': 'Malware Distribution Domain',
            'MI': 'Malware Distribution IP',
            'MU': 'Malware Distribution URL',
            'MC': 'Malware Command Center',
            'CA': 'Cyber Attack (Port Scan, Brute Force etc.)'
        }

        source_mapping = {
            'US': 'USOM',
            'SO': 'CERT',
            'RS': 'RSA',
            'IH': 'REPORTING'
        }

        desc_mapping = {
            'PH': 'The category containing malicious domain names, IP addresses, or links targeting social engineering attacks outside the finance sector.',
            'BP': 'It is the category that contains malicious domain names, IP addresses, or links specifically targeting the finance sector with social engineering attacks.',
            'MD': 'It is the category related to domain names where a portion or all of the malicious software is downloaded for execution.',
            'MI': 'It is the category related to IP addresses from which a portion or all of the malicious software is downloaded for execution.',
            'MU': 'It is the category related to links from which a portion or all of the malicious software is downloaded for execution.',
            'MC': 'It is the category containing domain names, IP addresses, or links used for malicious activities.',
            'CA': 'It is the category that regularly contains domain names, IP addresses, or links engaged in malicious activities.'
        }

        if raw_entry['type'] == 'domain' or raw_entry['type'] == 'ip':
            return {
                'data_id': raw_entry['id'],
                'data_type': raw_entry['type'],
                'address': raw_entry['url'],
                'mal_type': type_mapping.get(raw_entry['desc'], 'Not available'),
                'desc': desc_mapping.get(raw_entry['desc'], 'Not available'),
                'severity': raw_entry['criticality_level'],
                'source': source_mapping.get(raw_entry['source'], 'Not available'),
                'data_date': raw_entry['date'],
                'current_status': 'unblocked',
                'op_time': 'Not available',
                'update_date': update_date,
                'link': f"https://www.usom.gov.tr/adres/{raw_entry['id']}"
            }
    except Exception as e:
        print(f"Error filter_raw_entry: {e}")
        return None


def fill_table(raw_data):
    update_date = helper_methods.get_current_date()
    for raw_entry in raw_data:
        filtered_entry = filter_raw_entry(raw_entry, update_date)
        if filtered_entry:
            if not check_entry_exist(address=filtered_entry['address']):
                db_operations.save_to_table(entry=filtered_entry)


def check_entry_exist(address):
    entry = db_operations.get_entry_details(
        column_name='*',
        address=address)
    if entry:
        # Exist
        return True


def clear_old_data():
    today = helper_methods.get_current_date_utc().split()[0]
    data = db_operations.get_data_by_specified_condition(
        column_name='address,data_date',
        condition_column='current_status', 
        condition_value='"unblocked"')
    if data:
        for entry in data:
            if entry['data_date'].split()[0] != today:
                db_operations.remove_entry(address=entry['address'])