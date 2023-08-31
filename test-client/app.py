import json
import os
import urllib.parse
import urllib.request
from pprint import pprint

url = os.getenv("API_URL")

values = {"rooms": 2, "distance": 20}

data = urllib.parse.urlencode(values)
data = data.encode("ascii")  # data should be bytes
data = json.dumps(values).encode("utf-8")

try:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as f:
        res = f.read()
    pprint(res.decode())
except Exception as e:
    pprint(e)
