from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask.ext.cors import CORS
import requests
from . import config
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()

class TalkList(Resource):

    def get(self):
        print("Call for: GET /talks")
        url = config.es_base_url['talks']+'/_search'
        query = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        talks = []
        for hit in data['hits']['hits']:
            talk = hit['_source']
            talk['id'] = hit['_id']
            talks.append(talk)
        return talks

    def post(self):
        print("Call for: POST /talks")
        parser.add_argument('title')
        parser.add_argument('author')
        parser.add_argument('description')
        parser.add_argument('types', action='append')
        talk = parser.parse_args()
        print(talk)
        url = config.es_base_url['talks']
        resp = requests.post(url, data=json.dumps(talk))
        data = resp.json()
        return data

class Talk(Resource):

    def get(self, talk_id):
        print("Call for: GET /talks/%s" % talk_id)
        url = config.es_base_url['talks']+'/'+talk_id
        resp = requests.get(url)
        data = resp.json()
        talk = data['_source']
        return talk

    def put(self, talk_id):
        """TODO: update functionality not implemented yet."""
        pass

    def delete(self, talk_id):
        print("Call for: DELETE /talk/%s" % talk_id)
        url = config.es_base_url['talks']+'/'+talk_id
        resp = requests.delete(url)
        data = resp.json()
        return data

class Type(Resource):
    pass

class TypeList(Resource):

    def get(self):
        print("Call for /types")
        url = config.es_base_url['types']+'/_search'
        query = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        types = []
        for hit in data['hits']['hits']:
            type = hit['_source']
            type['id'] = hit['_id']
            types.append(type)
        return types

class Search(Resource):

    def get(self):
        print("Call for GET /search")
        parser.add_argument('q')
        query_string = parser.parse_args()
        url = config.es_base_url['talks']+'/_search'
        query = {
            "query": {
                "multi_match": {
                    "fields": ["title", "author", "description", "types"],
                    "query": query_string['q'],
                    "type": "cross_fields",
                    "use_dis_max": False
                }
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        talks = []
        for hit in data['hits']['hits']:
            talk = hit['_source']
            talk['id'] = hit['_id']
            talks.append(talk)
        return talks

api.add_resource(Talk, config.api_base_url+'/talks/<talk_id>')
api.add_resource(TalkList, config.api_base_url+'/talks')
api.add_resource(TypeList, config.api_base_url+'/types')
api.add_resource(Search, config.api_base_url+'/search')


