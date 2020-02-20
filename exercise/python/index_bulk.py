import json
from thailand_i18n import Tambons

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(["localhost:2222"])

tambons = Tambons()


def genBulk(docs):

    for doc in docs:
        yield {"_index": "thailand", "_id": doc['id'], 'pipeline': 'pipeline1', '_source': doc}
        #yield {"_index": "thailand", 'pipeline': 'pipeline1', '_source': doc}


if __name__ == "__main__":
    filename = 'thailand.json'
    size = 500

    with open(filename) as f:
        data = json.load(f)

    bulk_batch = []
    for n, line in enumerate(data):
        tid = line['district_code']
        try:
            i18n = tambons[str(tid)]
            bulk_batch.append({
                "id": n,
                "district_code": int(line['district_code']),
                "amphoe_code": int(line['amphoe_code']),
                "province_code": int(line['province_code']),
                "district": {
                    "en": i18n['tambon']['en'],
                    "th": line['district']
                },
                "amphoe": {
                    "en": i18n['amphoe']['en'],
                    "th": line['amphoe']
                },
                "province": {
                    "en": i18n['jhangwat']['en'],
                    "th": line['province']
                },
                "zipcode": str(line['zipcode']),
                "geo": i18n['geo']
            })
        except:
            bulk_batch.append({
                "id": n,
                "district_code": int(line['district_code']),
                "amphoe_code": int(line['amphoe_code']),
                "province_code": int(line['province_code']),
                "district": {
                    "th": line['district']
                },
                "amphoe": {
                    "th": line['amphoe']
                },
                "province": {
                    "th": line['province']
                },
                "zipcode": str(line['zipcode'])
            })
        if (n + 1) % size == 0:
            print('Batch:', n + 1)
            try:
                helpers.bulk(es, genBulk(bulk_batch))
                bulk_batch = []
            except Exception as e:
                print(str(e))
    print('End:', n + 1)
    helpers.bulk(es, genBulk(bulk_batch))
    print('Total', len(data))
