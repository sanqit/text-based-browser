import requests


def check_success(url):
    return "Success" if 200 <= requests.get(url).status_code < 400 else "Fail"
