# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# NOTE: Replace this with a valid host name.
host = "koqnamakersvc.azurewebsites.net/api/messages"

# NOTE: Replace this with a valid endpoint key.
# This is not your subscription key.
# To get your endpoint keys, call the GET /endpointkeys method.
endpoint_key = "64efdc6a-5fbb-4477-b6bc-d174a88d96cc"

# NOTE: Replace this with a valid knowledge base ID.
# Make sure you have published the knowledge base with the
# POST /knowledgebases/{knowledge base ID} method.
kb = "f071db60-afe0-4645-8116-5660ee0aa512"

method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

question = {
    'question': 'Do I need insurance?',
    'top': 3
}

def pretty_print (content):
# Note: We convert content to and from an object so we can pretty-print it.
	return json.dumps(json.loads(content), indent=4)

def get_answers (path, content):
	print ('Calling ' + host + path + '.')
	headers = {
		'Authorization': 'EndpointKey ' + endpoint_key,
		'Content-Type': 'application/json',
		'Content-Length': len (content)
	}
	conn = http.client.HTTPSConnection(host)
	conn.request ("POST", path, content, headers)
	response = conn.getresponse ()
	return response.read ()

# Convert the request to a string.
content = json.dumps(question)
result = get_answers (method, content)
print (pretty_print(result))