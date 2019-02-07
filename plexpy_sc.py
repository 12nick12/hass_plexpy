# This reports the stream count
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
stream_audio_bitrate_total = 0
stream_video_bitrate_total = 0
stream_bitrate_total = 0
print(stream_count)
