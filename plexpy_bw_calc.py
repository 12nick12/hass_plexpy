#!/usr/bin/env python

import json
import requests
import math

f = open("/home/hass/.homeassistant/python_scripts/plexpy/.creds", "r")
data = f.read().splitlines()
f.close()

host = data[4]
api_key = data[5]
url_base = data[6]
ssl = data[7]

if ssl == 'true':
    http = 'https'
if ssl == 'false':
    http = 'http'

url = http + "://" + host + "/" + url_base + "/api/v2?apikey=" + api_key + "&cmd=get_activity"

response = requests.get(url)

json_input = response.text

decoded = json.loads(json_input)

stream_count = decoded['response']['data']['stream_count']
stream_count = int(stream_count)
bandwidthTotal = 0

bw_total = decoded['response']['data']['total_bandwidth']
bw_total = float(bw_total) / 1024

#for i in range(0, stream_count):
#  bandwidth = decoded['response']['data']['sessions'][i]['bandwidth']
#  bandwidth =  float(bandwidth)
#  if bandwidth < 102400:
#    bandwidthTotal = bandwidthTotal + bandwidth / 1024

#print("%.2f" % bandwidthTotal)
print("%.2f" % bw_total)

