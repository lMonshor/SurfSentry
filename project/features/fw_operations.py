import concurrent.futures
import subprocess
from db.db_operations import *
from features.methods import get_current_date

def get_fw_data():
    resolved_ips = set()
    fw_data = {'items': []}
    today = get_current_date()
    data = get_data_by_column_name(column_name='url,resolved_ip', table_name="malicious_data")
    for item in data:
        if item[1] not in resolved_ips:
            resolved_ips.add(item[1])
            fw_data['items'].append({
                'url': item[0],
                'resolved_ip': item[1],
                'operation_time': today,
                'current_status': 'blocked'
            })
    return fw_data

def block_one_ip(target_ip,target_url):
        if not check_rule_existence(target_url):
            command = f"powershell netsh advfirewall firewall add rule name='Blocked by SurfSentry {target_url}' dir=out action=block remoteip={target_ip}"
            subprocess.run(command, shell=True)
        else:
            print(f"Already Exist: {target_url},{target_ip}")

def unblock_one_ip(target_url):
    if check_rule_existence(target_url):
        command = f"powershell netsh advfirewall firewall delete rule name='Blocked by SurfSentry {target_url}'"
        update_fw_rule(url=target_url, new_status='unblocked')
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while unblocking {target_url}: {e}")
    else:
        print("Not Exist")

def block_all_ips():
    try:
        fw_data = get_fw_data()
        clear_table_by_table_name("fw_rules")
        save_to_specified_table(data=fw_data, table_name="fw_rules")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(block_one_ip, target_ip=data['resolved_ip'], target_url=data['url']) for data in fw_data['items']]
        concurrent.futures.wait(futures)
    except Exception as e:
        print(f"An error occurred while blocking IPs: {e}")

def unblock_all_ips():
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(unblock_one_ip, target_url=data[0]) for data in get_data_by_column_name(column_name='url',table_name='fw_rules')] 
        concurrent.futures.wait(futures)
    except Exception as e:
        print(f"An error occurred while unblocking all IPs: {e}")

def check_rule_existence(target_url):
    try:
        command = f"powershell Get-NetFirewallRule -DisplayName 'Blocked by SurfSentry {target_url}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if "ObjectNotFound" in str(result):
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred while checking rule existence: {e}")

