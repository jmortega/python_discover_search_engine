
curl -XPOST 'http://localhost:9200/blog/posts' -d '{
    "title": "Discover python search engine",
    "published": "2017-09-22"
}'


curl -XPOST 'http://localhost:9200/blog/posts/_search?pretty=true -d '{
    "query": {
        "match": {
            "title": "python"
        }
    }
}'
