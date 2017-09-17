import json
import requests

url = "http://localhost:9200/pycones/talk/1"

document = {
  'title': "Discovering python search engine",
  'description' : "Full text search"
  }

requests.post(url, data=json.dumps(document))



