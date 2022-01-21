# -*- coding: utf-8 -*-

import json
from rich import print
from sfm.timer import DateTimeTimer
from opensearchpy.helpers import bulk
from pathlib_mate import Path
from learn_elasticsearch.os_domain import es_sanhe_prod as es

# --- Config
index = "write_throughput_test_1"


def read_data(nth: int):
    dir_here = Path(__file__).parent
    file = Path(dir_here, "data", "{}.json".format(str(nth).zfill(6)))
    data = json.loads(file.read_text())
    return data


def s1_delete_index():
    es.indices.delete(index=index, ignore=[400, 404])


def s2_create_index():
    mappings = {
        "properties": {
            "news_id": {"type": "keyword"},
            "url": {"type": "keyword"},
            "create_date": {"type": "keyword"},
            "author": {"type": "text"},
            "summary": {"type": "text"},
            "category": {"type": "keyword"},
        }
    }

    settings = {
        "index": {
            "number_of_replicas": 1,
            "number_of_shards": 10,
        }
    }

    body = {
        "mappings": mappings,
        "settings": settings,
    }

    es.indices.create(index=index, body=body, ignore=400)


def s3_bulk_index():
    def gen_data():
        for nth in range(1, 3 + 1):
            print(nth)
            data = read_data(nth)
            for doc in data:
                id = doc["news_id"]
                action = {
                    "_index": index,
                    "_id": id,
                    "_source": doc,
                }
                yield action

    with DateTimeTimer():
        bulk(es, gen_data())


def s4_search():
    body = {"query": {"match_all": {}}}
    res = es.count(index=index, body=body)
    print(res)


if __name__ == "__main__":
    # s1_delete_index()
    # s2_create_index()
    # s3_bulk_index()
    # s4_search()
    pass