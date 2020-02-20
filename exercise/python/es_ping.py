from elasticsearch import Elasticsearch

es = Elasticsearch(["localhost:2222"])

print(es.ping())
