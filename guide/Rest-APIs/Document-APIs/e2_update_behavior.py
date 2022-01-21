# -*- coding: utf-8 -*-

"""
在 ElasticSearch 中, 由于分布式, 基于内存的设计, 并不存在 Partial Update. 每一个 Update
本质上都是创建一个新的 version, 在服务器端 get 原始 document, 然后进行修改再保存.
"""

from rich import print
from learn_elasticsearch.tests import (
    es_sanhe_dev as es,
    reset_index,
)

index = "crud_examples"


# reset_index(es, index)

def multi_field_update():
    """
    同时 update 多个 field.
    """
    id = "test_multi_field_update"
    doc = {"name": "alice", "description": "this is alice", "value1": 0, "value2": 0}
    es.index(index=index, id=id, body=doc)

    res = es.get(index=index, id=id)
    print("--- before update ")
    print(res)

    # partial replacement
    update_body = {
        "doc": {
            "name": "bob",
            "description": "this is bob",
        },
    }
    es.update(index=index, id=id, body=update_body)
    print("--- after update 2 ")
    print(es.get(index=index, id=id))

    # serverside atomic update
    update_body = {
        "script": {
            "source": "ctx._source.value1 = ctx._source.value1 + params.increment1; ctx._source.value2 = ctx._source.value2 + params.increment2",
            "lang": "painless",
            "params": {
                "increment1": 1,
                "increment2": 2,
            }
        }
    }
    es.update(index=index, id=id, body=update_body)
    print("--- after update 1 ")
    print(es.get(index=index, id=id))


multi_field_update()
