import requests
from requests.exceptions import HTTPError

url_list = ['http://sejm.gov.pl', 'https://sejm.gov.pl']

for url in url_list:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http.err}')
    except Exception:
        print(f'Other error occured: {err}')
    else:
        print("success")