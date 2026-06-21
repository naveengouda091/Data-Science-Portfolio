import requests
import sys
import json

if len(sys.argv) !=2:
    sys.exit()

responce=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(responce.json(), indent=2))


o=responce.json()

for result in o["results"]:
    print(result["trackName"])