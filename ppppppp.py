import urllib.request as urllib2
import json
import datetime
import csv
import time

app_id = "272535582777707"
app_secret = "59e7ab31b01d3a5a90ec15a7a45a5e3b" # DO NOT SHARE WITH ANYONE!
page_id = 'nytimes'

access_token = app_id + "|" + app_secret


def testFacebookPageFeedData(page_id, access_token):
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id + "/feed" # changed
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    
    # retrieve data
    data = json.loads(request_until_succeed(url))
    
    print(json.dumps(data, indent=4, sort_keys=True))
    

testFacebookPageFeedData(page_id, access_token)