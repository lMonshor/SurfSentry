import subprocess
import db.db_operations
from features import helper_methods
import shutil
import threading
import os

ROOT_DRIVE = os.getenv('SystemRoot')
HOSTS_PATH = os.path.join(ROOT_DRIVE, "System32", "drivers", "etc", "hosts")
DEFAULT_HOSTS_CONTENT = """
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
"""


def check_acl_exist(address):
    try:
        command = f"powershell Get-NetFirewallRule -DisplayName 'Added by SurfSentry - {
            address}'"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        if result.returncode == 0:
            # Exist
            return True
    except Exception as e:
        print(f"Error check_acl_exist: {e}, {address}")


def check_hosts_exist(address):
    print(address)
    try:
        with open(HOSTS_PATH, 'r') as hosts_file:
            return any(line.strip() == f'#127.0.0.1 {address}' for line in hosts_file.readlines())
    except Exception as e:
        print(f'Error check_hosts_exist: {e}, {address}')


def add_entry(entry):
    if entry['data_type'] == 'ip':
        if not check_acl_exist(entry['address']):
            add_acl_entry(address=entry['address'])
        else:
            print(f'Already exist acl: {entry['address']}')
    elif entry['data_type'] == 'domain':
        if not check_hosts_exist(entry['address']):
            add_hosts_entry(entry['address'])
        else:
            print(f'Already exist hosts entry: {entry['address']}')


def remove_entry(entry):
    if entry['data_type'] == 'ip':
        if check_acl_exist(address=entry['address']):
            remove_acl_entry(address=entry['address'])
        else:
            print(f'Not exist acl: {entry['address']}')
    elif entry['data_type'] == 'domain':
        if check_hosts_exist(address=entry['address']):
            remove_hosts_entry(address=entry['address'])
        else:
            print(f'Not found hosts entry: {entry['address']}')


def add_acl_entry(address):
    try:
        operation_time = helper_methods.get_current_date()
        command = f"powershell netsh advfirewall firewall add rule name='Added by SurfSentry - {
            address}' dir=out action=allow remoteip={address}"
        subprocess.run(command, shell=True)
        db.db_operations.update_entry_status(
            address=address, new_status='blocked', op_time=operation_time)
    except Exception as e:
        print(f"Error add_acl_entry: {e}")


def add_hosts_entry(address):
    try:
        operation_time = helper_methods.get_current_date()
        with open(HOSTS_PATH, 'r+') as hosts_file:
            content = hosts_file.read()
            hosts_file.seek(0)
            hosts_file.write(f'#127.0.0.1 {address}\n{content}')
            db.db_operations.update_entry_status(
                address=address, new_status='blocked', op_time=operation_time)
    except Exception as e:
        print(f'Error add_hosts_entry: {e}, {address}')


def remove_acl_entry(address):
    try:
        operation_time = helper_methods.get_current_date()
        command = f"powershell netsh advfirewall firewall delete rule name='Added by SurfSentry - {
            address}'"
        subprocess.run(command, shell=True, check=True)
        db.db_operations.update_entry_status(
            address=address, new_status='unblocked', op_time=operation_time)
    except Exception as e:
        print(f"Error remove_acl_entry: {e}")


def remove_hosts_entry(address):
    try:
        operation_time = helper_methods.get_current_date()
        with open(HOSTS_PATH, 'r') as hosts_file:
            lines = hosts_file.readlines()
        with open(HOSTS_PATH, 'w') as hosts_file:
            for line in lines:
                if not (line.strip() == f'#127.0.0.1 {address}'):
                    hosts_file.write(line)
        db.db_operations.update_entry_status(
            address=address, new_status='unblocked', op_time=operation_time)
        print(f'Removed from hosts: {address}')
    except Exception as e:
        print(f'Error remove_hosts_entry: {e}, {address}')


def remove_all_entries():

    ip_adresses = db.db_operations.get_data_by_specified_condition(
        column_name='address',
        condition_column='current_status',
        condition_value='"blocked" AND data_type = "ip"')
    domain_addresses = db.db_operations.get_data_by_specified_condition(
        column_name='address',
        condition_column='current_status',
        condition_value='"blocked" AND data_type = "domain"')
    if ip_adresses:
        try:
            threads = []
            for entry in ip_adresses:
                thread = threading.Thread(
                    target=remove_acl_entry, args=(entry['address'],))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
        except Exception as e:
            print(f'Error remove_all_entries: {e}')

    if domain_addresses:
        clear_hosts(domain_addresses=domain_addresses)


def add_all_entries():
    try:
        ip_adresses = db.db_operations.get_data_by_specified_condition(
            column_name='address',
            condition_column='current_status',
            condition_value='"unblocked" AND data_type = "ip"')
        domain_addresses = db.db_operations.get_data_by_specified_condition(
            column_name='address',
            condition_column='current_status',
            condition_value='"unblocked" AND data_type = "domain"')
        if ip_adresses:
            threads = []
            for entry in ip_adresses:
                thread = threading.Thread(
                    target=add_acl_entry, args=(entry['address'],))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

        if domain_addresses:
            fill_hosts(domain_addresses)

    except Exception as e:
        print(f'Error add_all_entries: {e}')


def fill_hosts(domain_addresses):
    try:
        operation_time = helper_methods.get_current_date()
        with open(HOSTS_PATH, 'r+') as hosts_file:
            content = hosts_file.read()
            hosts_file.seek(0)
            for entry in domain_addresses:
                hosts_file.write(f'#127.0.0.1 {entry['address']}\n')
                db.db_operations.update_entry_status(
                    address=entry['address'], new_status='blocked', op_time=operation_time)
            hosts_file.write(content)

    except Exception as e:
        print(f'Error fill_hosts: {domain_addresses}')


def clear_hosts(domain_addresses):
    try:
        operation_time = helper_methods.get_current_date()

        with open(HOSTS_PATH, 'w') as hosts_file:
            hosts_file.write(DEFAULT_HOSTS_CONTENT)
            for entry in domain_addresses:
                db.db_operations.update_entry_status(
                    address=entry['address'], new_status='unblocked', op_time=operation_time)
        print("Hosts file restored to default.")
    except Exception as e:
        print(f"Error restore_hosts_default: {e}")


def start_protection():
    try:
        ip_adresses = db.db_operations.get_data_by_specified_condition(
            column_name='address',
            condition_column='current_status',
            condition_value='"blocked" AND data_type = "ip"')
        domain_addresses = db.db_operations.get_data_by_specified_condition(
            column_name='address',
            condition_column='current_status',
            condition_value='"blocked" AND data_type = "domain"')
        if ip_adresses:
            threads = []
            for entry in ip_adresses:
                thread = threading.Thread(
                    target=block_acl_entry, args=(entry['address'],))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

        if domain_addresses:
            romeve_hosts_prefix(domain_addresses)

    except Exception as e:
        print(f'Error start_protection: {e}')


def block_acl_entry(address):
    try:
        command = f"powershell netsh advfirewall firewall set rule name='Added by SurfSentry - {
            address}' new action=block"
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"Error update_acl_entry_action: {e}")


def romeve_hosts_prefix(domain_addresses):
    try:
        updated_lines = []
        with open(HOSTS_PATH, 'r') as hosts_file:
            lines = hosts_file.readlines()
            for line in lines:
                for entry in domain_addresses:
                    if line.strip() == f'#127.0.0.1 {entry['address']}':
                        line = line.lstrip('#')
                        break
                updated_lines.append(line)
        with open(HOSTS_PATH, 'w') as hosts_file:
            hosts_file.writelines(updated_lines)
    except Exception as e:
        print(f"Error romeve_hosts_prefix: {e}")


def stop_protection():
    try:
        ip_adresses = db.db_operations.get_data_by_specified_condition(
            column_name='address',
            condition_column='current_status',
            condition_value='"blocked" AND data_type = "ip"')
        domain_addresses = db.db_operations.get_data_by_specified_condition(
            column_name='address',
            condition_column='current_status',
            condition_value='"blocked" AND data_type = "domain"')
        if ip_adresses:
            threads = []
            for entry in ip_adresses:
                thread = threading.Thread(
                    target=unblock_acl_entry, args=(entry['address'],))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

        if domain_addresses:
            re_add_hosts_prefix(domain_addresses)

    except Exception as e:
        print(f'Error stop_protection: {e}')


def unblock_acl_entry(address):
    try:
        command = f"powershell netsh advfirewall firewall set rule name='Added by SurfSentry - {
            address}' new action=allow"
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"Error unblock_acl_entry: {e}")


def re_add_hosts_prefix(domain_addresses):
    try:
        updated_lines = []

        with open(HOSTS_PATH, 'r') as hosts_file:
            lines = hosts_file.readlines()

            for line in lines:
                for entry in domain_addresses:
                    if line.strip() == f'127.0.0.1 {entry['address']}':
                        line = '#' + line
                        break
                updated_lines.append(line)

        with open(HOSTS_PATH, 'w') as hosts_file:
            hosts_file.writelines(updated_lines)
    except Exception as e:
        print(f"Error re_add_hosts_prefix: {e}")


# def backup_hosts_file():
#     try:
#         shutil.copy(HOSTS_PATH,
#                     r'C:\\Windows\\System32\\drivers\\etc\\hosts_backup')
#         print('Backup successful')
#     except Exception as e:
#         print(f'Error backup_hosts_file: {e}')
