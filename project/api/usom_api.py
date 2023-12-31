import requests
import time
from features import helper_methods, data_filtering_operations
from db import db_operations
from ui.components import component_hcenterer


def make_request(request_url, retries=4):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json'
    }
    for _ in range(retries):
        try:
            response = requests.get(request_url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed to {request_url}: {e}")
            time.sleep(0.5)
            return None


def get_malicious_data(loading_ui=None):
    today = helper_methods.get_current_date_utc().split()[0]
    latest_date = db_operations.get_latest_entry_date()

    if latest_date:
        request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={
            latest_date}"

    else:
        request_url = f"https://www.usom.gov.tr/api/address/index?date_gte={
            today}"

    count_data = make_request(request_url=request_url)

    if count_data and "pageCount" in count_data and "totalCount" in count_data:
        page_count = count_data["pageCount"]
        total_count = count_data["totalCount"]

        if total_count > 1:
            for i in range(1, page_count+1):

                component_hcenterer.center_component_horizontally(
                    component=loading_ui.loading_title,
                    text=f"Getting Malicious Data from USOM Please Wait...\nPage: {
                        i}/{page_count}"
                )

                new_request_url = f"{request_url}&page={i}"
                raw_data = make_request(request_url=new_request_url)

                if raw_data is not None:
                    data_filtering_operations.fill_db(
                        raw_data['models'])