# -*- coding: utf-8 -*-

"""
Ref:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
"""

from rich import print
from opensearchpy.helpers import bulk
from learn_elasticsearch.tests import es_sanhe_dev as es
from learn_elasticsearch import helpers as hp

index = "crud_examples"


def bulk_index_update_delete():
    actions = [
        {
            "_op_type": "index",
            "_index": index,
            "_id": 1,
            "_source": {
                "name": "Alice",
                "balance": 0,
            }
        },
        {
            "_op_type": "update",
            "_index": index,
            "_id": 1,
            "script": {
                # "source": "cts._source.name = params.new_name; ctx._source.balance = ctx._source.balance + params.balance_increment",
                "source": "cts._source.name = params.new_name",
                "lang": "painless",
                "params": {
                    "new_name": "Bob",
                    # "balance_increment": 100,
                }
            }
        },
    ]

    res = bulk(es, actions)
    print(res)


def show_all():
    body = {"query": {"match_all": {}}}
    res = es.search(index=index, body=body)
    print(res)

# hp.reset_index(es, index)
bulk_index_update_delete()
# show_all()}{
