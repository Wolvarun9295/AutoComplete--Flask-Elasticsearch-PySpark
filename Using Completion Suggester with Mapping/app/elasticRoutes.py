from app import app
from flask_restful import Resource, Api, reqparse
from ES_Config import es, index


class ESsearch(Resource):
    def __init__(self):
        self.query = parser.parse_args().get("query", None)
        self.baseQuery = {
            "_source": "false",
            "size": 0,
            "suggest": {
                "auto": {
                    "prefix": "{}".format(self.query),
                    "completion": {
                        "field": "movies",
                        "skip_duplicates": "true",
                        "size": 10,
                        "fuzzy": {
                            "fuzziness": "auto"
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
