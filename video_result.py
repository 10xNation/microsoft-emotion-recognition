import httplib, urllib, base64, json

headers = {
    # Enter your subscription key
    "Ocp-Apim-Subscription-Key": "API_KEY",
    "Content-Type": "application/json"
}

# Enter the OID of the video you want the analysis results for
oid = "VIDEO_OID"

params = urllib.urlencode({})

try:
    conn = httplib.HTTPSConnection("westus.api.cognitive.microsoft.com")
    conn.request("GET", "/emotion/v1.0/operations/" + oid + "?%s" % params, "{}", headers)
    response = conn.getresponse()
    data = response.read()
    parsed = json.loads(data)
    print json.dumps(parsed, indent=4, sort_keys=True)
    conn.close()
except Exception as e:
    print str(e)
