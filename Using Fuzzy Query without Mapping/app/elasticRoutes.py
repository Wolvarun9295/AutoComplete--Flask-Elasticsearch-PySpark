from app import app
from flask_restful import Resource, Api, reqparse
from ES_Config import es, index


class ESsearch(Resource):
    def __init__(self):
        self.query = parser.parse_args().get("query", None)
        self.baseQuery = {
            "_source": [],
            "size": 0,
            "query": {
                "bool": {
                    "minimum_should_match": 1,
                    "should": [
                        {
                            "multi_match": {
                                "query": "{}".format(self.query),
                                "fuzziness": "AUTO",
                                "max_expansions": 50,
                                "prefix_length": 0,
                                "fuzzy_transpositions": "true",
                                "fields": ["movies", "movies.keyword"]
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "auto": {
                    "terms": {
                        "field": "movies.keyword",
                        "order": {
                            "_count": "desc"
                        }
                    }
                }
            }
        }

    def get(self):
        res = es.search(index=index_name, size=0, body=self.baseQuery)
        return res


api = Api(app)
index_name = index
parser = reqparse.RequestParser()
parser.add_argument("query", type=str, required=True)
api.add_resource(ESsearch, '/autocomplete')
