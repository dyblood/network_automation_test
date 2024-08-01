import requests
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

# payload = '''{}'''

# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
#     "Authorization": "application/json"
# }

#response = requests.request('POST', url, headers=headers, data = payload)

response = requests.post(url, auth=(user, pw)).json()

token = response['Token']

print(response.text.encode('utf8'))

