from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

index = 'movies'

mapping = {
    "mappings": {
        "properties": {
            "movies": {
                "type": "completion"
            }
        }
    }
}
