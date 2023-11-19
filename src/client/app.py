import json
import os
import urllib.parse
import urllib.request
from pprint import pprint
from urllib.error import HTTPError, URLError

url = os.getenv("API_URL")

VALUES = {"rooms": 2, "distance": 20}

DATA = urllib.parse.urlencode(VALUES)
DATA = DATA.encode("ascii")  # should be bytes
data = json.dumps(VALUES).encode("utf-8")

if __name__ == "__main__":
    try:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
            pprint(res.decode())
    except HTTPError as e:
        print("Error code: ", e.code)
    except URLError as e:
        pprint(e)
