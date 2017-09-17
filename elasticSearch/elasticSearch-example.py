from elasticsearch import Elasticsearch

es= Elasticsearch()

document = {"title":"pycones 2017","descripion":"discoverting python search engine"}

##create inded if doesnt already exist
response = es.index(index="myindex",doc_type="mydocument",id=2,body=document)
print(response)

##search for "python" in all fields in all documents
query = {'query':{'match':{'_all':'python'}}}
response_search = es.search(index="myindex",doc_type="mydocument",body=query)
print(response_search)
