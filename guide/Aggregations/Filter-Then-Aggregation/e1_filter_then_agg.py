# -*- coding: utf-8 -*-

"""
在 SQL 中有一种常用的操作是先通过 WHERE 进行 Filter, 然后对结果数据进行 Aggregation.
下面我们看看在 ES 中怎么做.
"""

from rich import print
import random
from opensearchpy.helpers import bulk
from learn_elasticsearch.os_domain import es_sanhe_dev as es

index = "aggregations_test"


def s01_reset_index():
    es.indices.delete(index=index, ignore=[400, 404])
    body = {
        "mappings": {
            "properties": {
                "timestamp": {"type": "long"},
                "category": {"type": "keyword"},
            }
        }
    }
    es.indices.create(index=index, body=body, ignore=[400, 404])


def s02_delete_data():
    body = {"query": {"match_all": {}}}
    res = es.delete_by_query(index=index, body=body)
    print(res)


def s03_prepare_data():
    n_doc = 1000
    actions = [
        {
            "_index": index,
            "_id": i,
            "_source": {
                "timestamp": random.randint(1, 1000),
                "category": "c{}".format(random.randint(1, 5))
            }
        }
        for i in range(1, 1 + n_doc)
    ]
    filtered_categories = [
        action["_source"]["category"]
        for action in actions
        if 400 <= action["_source"]["timestamp"] <= 600
    ]
    hist = {
        f"c{i}": 0
        for i in range(1, 1+5)
    }
    for cate in filtered_categories:
        hist[cate] += 1
    print(f"hist: {hist}")

    res = bulk(es, actions)
    print(res)


def s04_filter_then_agg():
    body = {
        "query": {
            "range": {
                "timestamp": {
                    "gte": 400,
                    "lte": 600,
                }
            }
        },
        "aggs": {
            "categories": {
                "terms": {"field": "category"}
            }
        }
    }
    res = es.search(index=index, body=body)
    print(res)


if __name__ == "__main__":
    # s01_reset_index()
    # s02_delete_data()
    # s03_prepare_data() # {'c1': 54, 'c2': 50, 'c3': 40, 'c4': 45, 'c5': 37}
    # s04_filter_then_agg()
    pass
