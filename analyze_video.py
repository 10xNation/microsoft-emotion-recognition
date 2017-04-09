import httplib, urllib, base64, json

headers = {
    # Enter your subscription key
    "Ocp-Apim-Subscription-Key": "API_KEY",
    "Content-Type": "application/json"
}

# Enter the URL of the video you want to analyze
body = "{ 'url': 'VIDEO_URL' }"

params = urllib.urlencode({})

try:
    conn = httplib.HTTPSConnection("westus.api.cognitive.microsoft.com")
    conn.request("POST", "/emotion/v1.0/recognizeinvideo?%s" % params, body, headers)
    response = conn.getresponse()
    location = response.getheader("Operation-Location");
    print(location)
    conn.close()
except Exception as e:
    print str(e)
