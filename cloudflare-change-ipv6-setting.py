# https://github.com/bddjr/cloudflare-change-ipv6-setting

import requests
import re, json

ON = input('value (on) or (off) :\n')
try:
    ON = str.lower(re.search('[a-zA-Z]+', ON).group())
except:
    print('Error: Can not find value from input')
    exit()
print()

TOKEN = input('TOKEN:\n')
if str.strip(TOKEN) == '':
    print('Error: Can not find TOKEN from input')
    exit()
print()

ZoneID = input('ZoneID or PatchURL: \n')
if str.strip(ZoneID) == '':
    print('Error: Can not find ZoneID from input')
    exit()
try:
    URL = re.search('https://.+', ZoneID).group()
except:
    URL = f'https://api.cloudflare.com/client/v4/zones/{ZoneID}/settings/ipv6'
print()

print('Requesting...')
r = requests.patch(
    url = URL ,
    data = '{"value":"%s"}' % (ON) ,
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+TOKEN
    }
)
if r.status_code >= 400:
    print(r.status_code, 'ERROR')
elif r.status_code >= 200 and r.status_code <= 299:
    print(r.status_code, 'OK')
else:
    print(r.status_code)
print(r.text)
r_json = json.loads(r.text)
print('success:', r_json['success'])
