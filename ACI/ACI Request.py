import requests
import json

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser":{
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}
headers = {
    'Content-Type': "application/json"
}

response = request.post(url, data=json.dumps(
    payload), header=headers, verify=False.json()
)

#print(json.dumps(response, indent=2, sort_keys=True))

#PARSE TOKEN AND SET COOKIE
token=response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC=cookie'] = token
