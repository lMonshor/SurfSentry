import requests
import time
from features import helper_methods, data_filtering_operations
from db import db_operations


def make_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json'
    }
    retries = 0
    while retries <= 4:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed to {url}: {e}")
            retries += 1
            time.sleep(0.5)
        return None


def get_malicious_data(loading_ui):
    today = helper_methods.get_previous_date_utc().split()[0]
    request_url = None
    data_filtering_operations.clear_old_data_from_mal_data()
    last_data_date = data_filtering_operations.get_last_mal_data_date()
    if last_data_date:
        request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={
            last_data_date}"
    else:
        db_operations.clear_table_by_table_name('malicious_data')
        request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={
            today}"
    
    page_count_data = make_request(request_url)
    
    if page_count_data is not None:
        page_count = page_count_data["pageCount"]
        total_count = page_count_data["totalCount"]
        if total_count > 1:
            for i in range(1, page_count+1):
                loading_ui.loading_title.setText(
                    f"Getting Malicious Data from USOM Please Wait...\nPage: {i}/{page_count}")
                loading_ui.loading_title.adjustSize()
                request_url = f"{request_url}&page={i}"
                data = make_request(request_url)
                if data is not None:
                    data_filtering_operations.fill_mal_data_table(data['models'])
            # information_ui.information_title.setText(f"{total_count} Malicious Data have been updated.")
            # information_ui.information_title.adjustSize()
            
        # else:
        #     information_ui.information_title.setText("New Malicious Data is not available.")
        #     information_ui.information_title.adjustSize()
    else:
        return None
