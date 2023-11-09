import subprocess
import db.db_operations
from features import methods,workers
import shutil
import threading


def block_unblock(selected_blocked_item_detail, sender,my_loading_ui,my_information_ui,fillBlockedList):
    try:
        my_blocking_op_worker = workers.BlockingOperationWorker(
            selected_blocked_item_detail, sender)
        if sender.find("all") != -1:
            print("inside condition" , sender)
            if not my_loading_ui.isVisible():
                print("show")
                my_loading_ui.show()
            my_blocking_op_worker.finished.connect(my_loading_ui.hide)
            my_blocking_op_worker.finished.connect(my_information_ui.show)
        my_blocking_op_worker.finished.connect(fillBlockedList)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)
        my_blocking_op_worker.start()
    except Exception as e:
        print(f"Error block_unblock: {e}")


def backup_hosts_file():
    try:
        shutil.copy(r'C:\\Windows\\System32\\drivers\\etc\\hosts',
                    r'C:\\Windows\\System32\\drivers\\etc\\hosts_backup')
        print('Backup successful')
    except Exception as e:
        print(f'Error backup_hosts_file: {e}')


def check_acl_existence(target_url):
    try:
        command = f"powershell Get-NetFirewallRule -DisplayName 'Blocked by SurfSentry {
            target_url}'"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        if result.returncode == 0:
            # Exist
            return True
        else:
            return False
    except Exception as e:
        print(f"Error check_rule_existence: {e}, {target_url}")


def check_hosts_rule_existence(target_url):
    try:
        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as hosts_file:
            return any(line.strip() == f'127.0.0.1 {target_url}' for line in hosts_file.readlines())
    except Exception as e:
        print(f'Error check_hosts_rule_existence: {e}, {target_url}')


def add_acl_entry(target_url):
    try:
        operation_time = methods.get_current_date()
        command = f"powershell netsh advfirewall firewall add rule name='Blocked by SurfSentry {
            target_url}' dir=out action=block remoteip={target_url}"
        subprocess.run(command, shell=True)
        db.db_operations.update_blocked_table(
            url=target_url, new_status='blocked', op_time=operation_time)
    except Exception as e:
        print(f"Error add_to_fw_rule: {e}")


def add_acl_entries(target_data):
    threads = []
    for item in target_data:
        target_url = item[0]
        thread = threading.Thread(target=add_acl_entry, args=(target_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def remove_acl_entry(target_url):
    try:
        operation_time = methods.get_current_date()
        command = f"powershell netsh advfirewall firewall delete rule name='Blocked by SurfSentry {
            target_url}'"
        db.db_operations.update_blocked_table(
            url=target_url, new_status='unblocked', op_time=operation_time)
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"Error remove_from_fw_rule: {e}")


def remove_acl_entries(target_data):
    threads = []
    for item in target_data:
        target_url = item[0]
        thread = threading.Thread(target=remove_acl_entry, args=(target_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def add_entry_to_hosts_file(target_url):
    try:
        operation_time = methods.get_current_date()
        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'r+') as hosts_file:
            content = hosts_file.read()
            hosts_file.seek(0)
            hosts_file.write(f'127.0.0.1 {target_url}\n{content}')
        db.db_operations.update_blocked_table(
            url=target_url, new_status='blocked', op_time=operation_time)
        print(f'Added to hosts: {target_url}')
    except Exception as e:
        print(f'Error add_to_hosts_file: {e}, {target_url}')


def add_entries_to_hosts_file(target_urls):
    try:
        operation_time = methods.get_current_date()
        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'r+') as hosts_file:
            content = hosts_file.read()
            hosts_file.seek(0)

            for target_url in target_urls:
                hosts_file.write(f'127.0.0.1 {target_url}\n')

            hosts_file.write(content)

        for target_url in target_urls:
            db.db_operations.update_blocked_table(
                url=target_url, new_status='blocked', op_time=operation_time)

        print(f'Added to hosts: {", ".join(target_urls)}')
    except Exception as e:
        print(f'Error add_to_hosts_file_all_data: {
              e}, {", ".join(target_urls)}')


def remove_entry_from_hosts_file(target_url):
    try:
        operation_time = methods.get_current_date()
        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as hosts_file:
            lines = hosts_file.readlines()
        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'w') as hosts_file:
            for line in lines:
                if not (line.strip() == f'127.0.0.1 {target_url}'):
                    hosts_file.write(line)
        db.db_operations.update_blocked_table(
            url=target_url, new_status='unblocked', op_time=operation_time)
        print(f'Removed from hosts: {target_url}')
    except Exception as e:
        print(f'Error remove_from_hosts_file: {e}, {target_url}')


def remove_entries_from_hosts_file(target_urls):
    try:
        operation_time = methods.get_current_date()
        updated_lines = []

        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as hosts_file:
            lines = hosts_file.readlines()

            for line in lines:
                if not any(line.strip() == f'127.0.0.1 {url}' for url in target_urls):
                    updated_lines.append(line)

        with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'w') as hosts_file:
            hosts_file.writelines(updated_lines)

        for target_url in target_urls:
            db.db_operations.update_blocked_table(
                url=target_url, new_status='unblocked', op_time=operation_time)
        print(f'Removed to hosts: {", ".join(target_urls)}')

    except Exception as e:
        print(f'Error remove_from_hosts_file: {e}, {target_urls}')


def block_entry(target_data):
    try:
        target_url = target_data[0]
        if target_data[1] == 'ip':
            if not check_acl_existence(target_url):
                add_acl_entry(target_url)
            else:
                print(f'Already exist fw rule: {target_url}')
        elif target_data[1] == 'domain':
            if not check_hosts_rule_existence(target_url):
                add_entry_to_hosts_file(target_url)
            else:
                print(f'Already exist hosts rule: {target_url}')
    except Exception as e:
        print(f'Error block_one_data: {e}, {target_data}')


def block_all_entries():
    try:
        data = db.db_operations.custom_query(
            'select url,data_type from blocked_data where current_status = "unblocked"')
        if data:
            target_urls = [item[0] for item in data if item[1] == 'domain']
            add_entries_to_hosts_file(target_urls)
            target_data = [item for item in data if item[1] == 'ip']
            add_acl_entries(target_data)
        else:
            print('No unblocked data block_all_data')
    except Exception as e:
        print(f'Error block_all_data: {e}')


def unblock_entry(target_data):
    try:
        target_url = target_data[0]
        if target_data[1] == 'ip':
            if check_acl_existence(target_url):
                remove_acl_entry(target_url)
            else:
                print(f'Not exist fw rule: {target_url}')
        elif target_data[1] == 'domain':
            if check_hosts_rule_existence(target_url):
                remove_entry_from_hosts_file(target_url)
            else:
                print(f'Not found hosts rule: {target_url}')
    except Exception as e:
        print(f'Error unblock_one_data: {e}, {target_data}')


def unblock_all_entries():
    try:
        data = db.db_operations.custom_query(
            'select url,data_type from blocked_data where current_status = "blocked"')
        if data:
            target_urls = [item[0] for item in data if item[1] == 'domain']
            remove_entries_from_hosts_file(target_urls)
            target_data = [item for item in data if item[1] == 'ip']
            remove_acl_entries(target_data)
        else:
            print('No blocked data to unblock_all_data')
    except Exception as e:
        print(f'Error unblock_all_data: {e}')
