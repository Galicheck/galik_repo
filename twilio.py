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


url = 'https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms'
client_id = AC29a245d297cdb258090968f49a3032d8
client_secret = dcab90574c1b1d73ff5616a0eaefdcd1

response = requests.get(url, auth=(client_id,client_secret))

data = {'To': '+48515417186',
        'From': '+13344543966',
        'Body': 'Nie mam pomysłu'}
response = requests.get(url, auth=(client_id,client_secret), data= data)

response.status_code