#!/usr/bin/env python

import json
import requests
import math

host = 'host.site'
api_key = 'api_key_from_plexpy'
url_base = 'url_base_with_beginning_slash_leave_blank_if_nothin'
ssl = 'true_or_false_for_ssl'

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
print("Stream Count: %.0f" % stream_count)

for i in range(0, stream_count):
    transcode = decoded['response']['data']['sessions'][i]['transcode_decision']
    user = decoded['response']['data']['sessions'][i]['user']
    bandwidth = decoded['response']['data']['sessions'][i]['bandwidth']  
    bandwidthTotal = float(bandwidthTotal) + float(bandwidth) / 1024
    print("Type of Stream: %s" % transcode)
    print("User: %s:" % user)

