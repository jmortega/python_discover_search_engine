import requests
import json

def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "title": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['title']))
        
if __name__ == '__main__':
    uri_search = 'http://localhost:9200/pycones/talk/_search'
    results = search(uri_search, "python")
    format_results(results)




