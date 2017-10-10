#!/usr/bin/env python

import json
import requests

host = 'host.site'
api_key = 'api_key_from_plexpy'
url_base = 'url_base_with_beginning_slash_leave_blank_if_nothin'
ssl = 'true_or_false_for_ssl'

if ssl == 'true':
    http = 'https'
if ssl == 'false':
    http = 'http'

url = http + "://" + host + url_base + "/api/v2?apikey=" + api_key + "&cmd=get_activity"

requests.packages.urllib3.disable_warnings()

response = requests.get(url, verify=False)

json_input = response.text

decoded = json.loads(json_input)

stream_count = decoded['response']['data']['stream_count']
stream_count = int(stream_count)

print(stream_count)
