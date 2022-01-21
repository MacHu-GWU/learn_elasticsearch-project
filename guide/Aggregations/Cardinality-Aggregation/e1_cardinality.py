# -*- coding: utf-8 -*-

"""
测试 Cardinality Aggregation 的功能.
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
                "name": {"type": "keyword"},
                "category": {"type": "text", "fielddata": True},
            }
        }
    }
    es.indices.create(index=index, body=body, ignore=[400, 404])


def s02_delete_data():
    body = {"query": {"match_all": {}}}
    res = es.delete_by_query(index=index, body=body)
    print(res)


def s03_prepare_data():
    n_name = 500
    n_category = 10
    n_doc = 1000
    actions = [
        {
            "_index": index,
            "_id": i,
            "_source": {
                "name": "name{}".format(random.randint(1, n_name)),
                "category": "category{}".format(random.randint(1, n_category)),
            }
        }
        for i in range(1, 1 + n_doc)
    ]
    res = bulk(es, actions)
    print(res)


def s04_cardinality_agg():
    body = {
        "aggs": {
            "category_count": {
                "cardinality": {
                    "field": "category"
                }
            }
        }
    }
    res = es.search(index=index, body=body)
    print(res)

    body = {
        "aggs": {
            "category_count": {
                "cardinality": {
                    "field": "name"
                }
            }
        }
    }
    res = es.search(index=index, body=body)
    print(res)


if __name__ == "__main__":
    # s01_reset_index()
    # s02_delete_data()
    # s03_prepare_data()
    # s04_cardinality_agg()
    pass
