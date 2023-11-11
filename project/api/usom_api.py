import requests
import time
from features import methods
from db import db_operations

def make_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json'
    }
    retries=0
    while retries <=4:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed to {url}: {e}")
            retries +=1
            time.sleep(0.5)
        return None

def get_malicious_data(loading_ui):
    today = methods.get_current_date_utc().split()[0]
    last_update_date = db_operations.custom_query("select date from malicious_data where id = 1")
    request_url = None
    if last_update_date:
        last_update_date = last_update_date[0][0]
        if last_update_date.split()[0] == today:
            last_data_date = db_operations.custom_query("select date from malicious_data order by data_id desc limit 1")
            if last_data_date:
                last_data_date = last_data_date[0][0]
                request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={last_data_date}"
    else:
        db_operations.clear_table_by_table_name('malicious_data')
        request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={today}"  
    data = make_request(request_url)
    if data is not None and "pageCount" in data:
        pageCount = data["pageCount"]
        raw_data = []
        for i in range(1,pageCount+1):
            loading_ui.dialog_loading_title.setText(f"Getting Malicious Data from USOM page: {pageCount}/{i}. Please Wait...")
            request_url = f"{request_url}&page={i}"
            data = make_request(request_url)
            if data is not None:
                raw_data.extend(data['models'])
        methods.fill_mal_data_table(raw_data)
    else:
        return None