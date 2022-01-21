# -*- coding: utf-8 -*-

"""
根据 query 把 match 到的 document 删除.
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


def show_all():
    body = {
        "from": 0,
        "size": 50,
        "query": {"match_all": {}}
    }
    res = es.search(index=index, body=body)
    print(res)


# hp.reset_index(es, index)
# bulk_insert()
# delete_by_query()
# show_all()
