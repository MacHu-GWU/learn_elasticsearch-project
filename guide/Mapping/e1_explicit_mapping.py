# -*- coding: utf-8 -*-

from rich import print
from learn_elasticsearch.os_domain import es_sanhe_dev as es
from learn_elasticsearch import helpers as hp

index = "explicit_mapping_test"


def s01_delete_index():
    res = es.indices.delete(index=index, ignore=[400, 401])
    print(res)


def s02_create_index():
    body = {
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "email": {"type": "keyword"},
                "age": {"type": "integer"},
            }
        }
    }
    res = es.indices.create(index=index, body=body)
    print(res)


def s03_get_mapping():
    res = es.indices.get_mapping(index=index)
    print(res)


if __name__ == "__main__":
    # s01_delete_index()
    # s02_create_index()
    s03_get_mapping()
    pass
