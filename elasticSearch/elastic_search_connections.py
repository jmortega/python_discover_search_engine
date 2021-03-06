import elasticsearch
# client using all the defaults: localhost:9200 and http urllib3 transport
es = elasticsearch.Elasticsearch()

# client using localhost:9200 and http requests transport
from elasticsearch.connection import RequestsHttpConnection
es = elasticsearch.Elasticsearch(sniff_on_start=True, connection_class=RequestsHttpConnection)

# client using a node with sniffing and thrift protocol
from elasticsearch.connection import ThriftConnection
es = elasticsearch.Elasticsearch(["search1:9500"], sniff_on_start=True, connection_class=ThriftConnection)

# client using a node with sniffing and memcached protocol
from elasticsearch.connection import MemcachedConnection
es = elasticsearch.Elasticsearch(["search1:11211"], sniff_on_start=True, connection_class=MemcachedConnection)



