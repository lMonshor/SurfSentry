import subprocess
from db import db_operations
from features import helper_methods
import threading
import os

ROOT_DRIVE = os.getenv('SystemRoot')
HOSTS_PATH = os.path.join(ROOT_DRIVE, "System32", "drivers", "etc", "hosts")


def update_hosts_file(action, address=None, domain_addresses=None):
    try:
        operation_time = helper_methods.get_current_date()
        with open(HOSTS_PATH, 'r+') as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)

            if action in ['add', 'remove']:
                domains = [address]
            else:
                domains = domain_addresses

            if action in ['add', 'fill']:
                for addr in domains:
                    hosts_file.write(f'#127.0.0.1 {addr}\n')
                    db_operations.update_entry_status(
                        address=addr, new_status='blocked', op_time=operation_time)
                    print(f'added domain: {addr}\n')

                hosts_file.writelines(lines)

            elif action in ['remove', 'clear']:
                modified_lines = []

                for line in lines:
                    found = False
                    for addr in domains:
                        if '127.0.0.1' in line:
                            if addr == line.split()[1]:
                                db_operations.update_entry_status(
                                    address=addr, new_status='unblocked', op_time=operation_time)
                                print(f'removed domain: {addr}\n')
                                found = True
                                break
                    if not found:
                        modified_lines.append(line)

                hosts_file.writelines(modified_lines)

            hosts_file.truncate()

    except Exception as e:
        print(f'Error in update_hosts_file: {e}')


def modify_hosts_prefix(action, domain_addresses):
    try:
        with open(HOSTS_PATH, 'r+') as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)
            modified_lines = []
            hosts_file.truncate()
            for line in lines:
                for addr in domain_addresses:
                    if action == 'block':
                        if line.strip() == f'#127.0.0.1 {addr}':
                            line = line.lstrip('#')
                            break

                    elif action == 'unblock':
                        if line.strip() == f'127.0.0.1 {addr}':
                            line = '#' + line
                            break

                modified_lines.append(line)

            hosts_file.writelines(modified_lines)

    except Exception as e:
        print(f"Error modify_hosts_prefix: {e}")


def manage_entry(entry, action):
    operation_time = helper_methods.get_current_date()
    entry_data_type = entry['data_type']
    address = entry['address']
    if entry_data_type == 'ip':
        command = None
        new_status = None

        if (action == 'add' or action == 'fill'):
            command = f"powershell netsh advfirewall firewall add rule name='Added by SurfSentry - {
                address}' dir=out action=allow remoteip={address}"
            new_status = 'blocked'

        elif (action == 'remove' or action == 'clear'):
            command = f"powershell netsh advfirewall firewall delete rule name='Added by SurfSentry - {
                address}'"
            new_status = 'unblocked'

        elif action == 'block':
            command = f"powershell netsh advfirewall firewall set rule name='Added by SurfSentry - {
                address}' new action=block"

        elif action == 'unblock':
            command = f"powershell netsh advfirewall firewall set rule name='Added by SurfSentry - {
                address}' new action=allow"

        if command:
            try:
                subprocess.run(command, shell=True, check=True)
                if new_status:
                    db_operations.update_entry_status(
                        address=address, new_status=new_status, op_time=operation_time)
                    print(f'added acl: {address}')
            except subprocess.CalledProcessError as e:
                print(f"Error manage_entry: {e} while {action} for {address}")

    elif entry_data_type == 'domain':
        if action == 'add' or action == 'remove':
            update_hosts_file(action=action, address=address)


def manage_all_entries(action, condition_value):
    data = db_operations.get_data_by_specified_condition(
        column_name='address,data_type',
        condition_column='current_status',
        condition_value=condition_value)
    if data:
        threads = []
        domain_addresses = []
        for entry in data:
            entry_data_type = entry['data_type']
            addr = entry['address']
            if entry_data_type == 'ip':
                thread = thread = threading.Thread(
                    target=manage_entry, args=(entry, action,)
                )
                threads.append(thread)
                thread.start()

            elif entry_data_type == 'domain':
                domain_addresses.append(addr)

        for thread in threads:
            thread.join()
        if domain_addresses:
            if action == 'fill' or action == 'clear':
                update_hosts_file(
                    action=action, domain_addresses=domain_addresses)

            elif action == 'block' or action == 'unblock':
                modify_hosts_prefix(
                    action=action, domain_addresses=domain_addresses)
