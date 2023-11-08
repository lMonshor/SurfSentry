import requests
import time
import features.methods
#from features.methods import process_malicious_data,get_current_date_utc,get_previous_date_utc

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
    yesterday = features.methods.get_previous_date_utc().split()[0]
    request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={yesterday}"
    data = make_request(request_url)
    if data is not None and "pageCount" in data:
        pageCount = data["pageCount"]
        raw_data = []
        for i in range(1,pageCount+1):
            loading_ui.dialog_loading_title.setText(f"Getting Malicious Data from USOM page: {pageCount}/{i}. Please Wait...")
            request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={yesterday}&page={i}"
            data = make_request(request_url)
            if data is not None:
                raw_data.extend(data['models'])
        features.methods.process_malicious_data(raw_data)
    else:
        return None
