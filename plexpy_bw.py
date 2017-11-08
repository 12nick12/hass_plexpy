#!/usr/bin/env python
# This reports the total bandwidth used.
import json
import requests
import math

host = ''
api_key = ''
url_base = 'not including slashes'
ssl = 'true/false'

if ssl == 'true':
    http = 'https'
if ssl == 'false':
    http = 'http'

url = http + "://" + host + "/" + url_base + "/api/v2?apikey=" + api_key + "&cmd=get_activity"

requests.packages.urllib3.disable_warnings()

response = requests.get(url, verify=False)

json_input = response.text

decoded = json.loads(json_input)

stream_count = decoded['response']['data']['stream_count']
stream_count = int(stream_count)
bandwidthTotal = 0

for i in range(0, stream_count):
    bandwidth = decoded['response']['data']['sessions'][i]['bandwidth']
    bandwidthTotal = float(bandwidthTotal) + float(bandwidth) / 1024

print("%.2f" % bandwidthTotal)
