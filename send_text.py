import requests
from requests.auth import HTTPBasicAuth
to_number = '+13345590810'
from_number = '+18583143422'
message = ''
account_sid = 'AC007b71381af2a1c9351372424c132b19'
auth_token = '49c355c3c07da11bf2b47b27bc48b750'
auth = HTTPBasicAuth(account_sid, auth_token)
url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages'.format(account_sid)
values = {  
        'To' : +13345590810, 
        'From' : +18583143422,
        'Body' : message,
        }
response = requests.post(url, data = values, auth = auth)

