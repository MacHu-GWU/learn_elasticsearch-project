# -*- coding: utf-8 -*-

"""
计算 query 所 match 到的 documents 的总数.

Ref:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/search-count.html
"""

from rich import print
from opensearchpy.helpers import bulk
from learn_elasticsearch.tests import es_sanhe_dev as es
from learn_elasticsearch import helpers as hp

index = "crud_examples"


def bulk_insert():
    def gen_actions():
        n = 1000
        for i in range(1, 1 + n):
            yield {
                "_index": index,
                "_id": i,
                "_source": {
                    "name": f"user_{i}",
                }
            }

    res = bulk(es, gen_actions())
    print(res)


def delete_by_query():
    body = {"query": {"match_all": {}}}
    res = es.delete_by_query(index=index, body=body)
    print(res)


def count_matched():
    body = {
        "query": {"match_all": {}}
    }
    res = es.count(index=index, body=body)
    print(res)

# hp.reset_index(es, index)
# bulk_insert()
# count_matched()
