#!/usr/bin/env python
# This reports the stream count

import json
import requests
import math

host = ''
api_key = ''
url_base = 'not included slashes'
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
stream_audio_bitrate_total = 0
stream_video_bitrate_total = 0
stream_bitrate_total = 0
print(stream_count)
