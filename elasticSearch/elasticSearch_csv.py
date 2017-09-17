import csv
from elasticsearch import ElasticSearch

#by default connect with localhost:9200
es = ElasticSearch()

#create an index in es,ignore status code 400
es.indices.create(index='myindex',ignore=400)

with open('data.csv') as file:
  reader = csv.DictReader(file)
  for line in reader:
    es.index(index='myindex',doc_type,body=line)


