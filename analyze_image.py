import httplib, urllib, base64, json

headers = {
    # Enter your subscription key
    "Ocp-Apim-Subscription-Key": "API_KEY",
    "Content-Type": "application/json"
}

# Enter the URL of the image you want to analyze
body = "{ 'url': 'IMAGE_URL' }"

params = urllib.urlencode({})

try:
    conn = httplib.HTTPSConnection("westus.api.cognitive.microsoft.com")
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    parsed = json.loads(data)
    print json.dumps(parsed, indent=4, sort_keys=True)
    conn.close()
except Exception as e:
    print str(e)
