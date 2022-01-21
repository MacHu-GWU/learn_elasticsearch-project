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


def bulk_index():
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


def show_all():
    body = {"query": {"match_all": {}}}
    res = es.search(index=index, body=body)
    print(res)


# hp.reset_index(es, index)
# bulk_index()
# show_all()
