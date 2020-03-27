import requests
import os
import json
#
#print(os.environ['keyword_browserstack_user'])
#print(os.environ['keyword_browserstack_token'])
basicAuthCredentials = (os.environ['keyword_browserstack_user'], os.environ['keyword_browserstack_token'])

# Send HTTP GET request to server and attempt to receive a response
response = requests.get('https://api.browserstack.com/automate/plan.json', auth=basicAuthCredentials)
#print(response.status_code)
# If the HTTP GET request can be served
if response.status_code == 200:
        #print(response.text)
        data = json.loads(response.text)
        print json.dumps(data)


