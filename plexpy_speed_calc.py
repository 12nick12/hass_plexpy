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

#print(decoded)
stream_count = decoded['response']['data']['stream_count']
stream_count = int(stream_count)
stream_count_transcode = 0
SpeedTotal = 0
Speed = 0
Transcode = "copy"
Throttled = 0

for i in range(0, stream_count):
  Transcode = decoded['response']['data']['sessions'][i]['stream_video_decision']
  Throttled = decoded['response']['data']['sessions'][i]['transcode_throttled']
  if Transcode == "transcode" and Throttled == 0:
    Speed = decoded['response']['data']['sessions'][i]['transcode_speed']
    stream_count_transcode = stream_count_transcode + 1
    SpeedTotal = float(SpeedTotal) + float(Speed) / stream_count_transcode
print("%.2f" % SpeedTotal)
