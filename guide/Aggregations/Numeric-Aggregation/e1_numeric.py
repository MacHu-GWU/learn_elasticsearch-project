# -*- coding: utf-8 -*-

"""
测试 Average, Min, Max 等基于数值计算的 Aggregation 的功能.
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
                "value": {"type": "long"},
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
                "value": random.randint(1, 1000000),
            }
        }
        for i in range(1, 1 + n_doc)
    ]
    values = [action["_source"]["value"] for action in actions]
    total = sum(values)
    minimum = min(values)
    maximum = max(values)
    average = total / n_doc
    print(f"avg = {average}, min = {minimum}, max = {maximum}")
    res = bulk(es, actions)
    print(res)


def s04_avg_min_max_agg():
    body = {
        "aggs": {
            "average": {
                "avg": {"field": "value"}
            },
            "minimum": {
                "min": {"field": "value"}
            },
            "maximum": {
                "max": {"field": "value"}
            },
            "median_absolute_deviation": {
                "max": {"field": "value"}
            },
            "percentiles": {
                "percentiles": {"field": "value"}
            },
            "percentile_ranks": {
                "percentile_ranks": {"field": "value", "values": [500000, ]}
            },
            # "boxplot": { # OpenSearch 还不支持
            #     "boxplot": {"field": "value"}
            # }
            "value_count": {"value_count": {"field": "value"}}
        }
    }
    res = es.search(index=index, body=body)
    print(res)


if __name__ == "__main__":
    # s01_reset_index()
    # s02_delete_data()
    # s03_prepare_data() # avg = 497327.78, min = 1658, max = 998685
    # s04_avg_min_max_agg()
    pass
