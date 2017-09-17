from whoosh import fields, index

from datetime import datetime

'''class whooshSCHEMA(fields.SchemaClass):
  title = fields.TEXT(stored=True,sortable=True)
  content =  fields.TEXT(spelling=True)
  date = fields.DATETIME(stored=True)
  summary = fields.STORED
  url=fields.ID(stored=True, unique=True))'''

WHOOSH_SCHEMA = fields.Schema(
  title=fields.TEXT(stored=True,sortable=True),
  content=fields.TEXT(spelling=True),
  date = fields.DATETIME(stored=True),
  summary = fields.STORED,
  url=fields.ID(stored=True, unique=True))

#To create an index basically you need a writer object
ix = index.create_in("index",schema=WHOOSH_SCHEMA)
writer = ix.writer()

writer.add_document(title="pycones 2017",content="python conference",
  date = datetime(2017,9,22),
  summary = "discovering python search engine",
  url="http://pycones.es")

writer.add_document(title="python 2017",content="pycones2017",
  date = datetime(2017,9,22),
  summary = "discovering python search engine",
  url="http://pycones.es")

writer.commit()  

#searching in the index by a single field
from whoosh import qparser

queryParser = qparser.QueryParser("content",schema = ix.schema)
query = queryParser.parse("python")
with ix.searcher() as searcher:
  results = searcher.search(query)
  print(results)
  for result in results:
    print(result)

#searching in the index by a multiple field
from whoosh.qparser import MultifieldParser, OrGroup

queryParser = MultifieldParser(["title", 
                       "content"],
                        schema = ix.schema,
                        group = OrGroup)
query = queryParser.parse("python")
with ix.searcher() as searcher:
  results = searcher.search(query)
  print(results)
  for result in results:
    print(result)
