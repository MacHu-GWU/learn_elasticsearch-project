# -*- coding: utf-8 -*-

"""
测试方法:

1. 执行 s1, s2, s3 确保 document 被创建, 并且 value = 0
2. 打开两个 terminal 输入 python e3_concurrent_update.py
3. 快速在两个 terminal 按下 enter 运行. 效果是对 value 进行 1000 次 +1, 由于有两个
    并发, 所以互相之间会争抢
4. 执行 s4, 查看 value 是否是 2000

ES 中处理并发的策略详解 https://www.elastic.co/guide/en/elasticsearch/reference/current/optimistic-concurrency-control.html
"""

from rich import print
from learn_elasticsearch.tests import (
    es_sanhe_dev as es,
    create_index, delete_index,
)

index = "concurrent_update_test"
id_ = 1


def s1_create_initial_doc():
    print(es.index(index=index, id=id_, body={"value": 0}))


def s2_inspect_doc():
    print(es.get(index=index, id=id_))


def s3_update():
    for i in range(1000):
        print(f"{i}th update ...")
        body = {
            "script": {
                "source": "ctx._source.value = ctx._source.value + params.increment",
                "lang": "painless",
                "params": {
                    "increment": 1,
                }
            }
        }
        res = es.update(index=index, id=id_, body=body, retry_on_conflict=5)
        print(res)


if __name__ == "__main__":
    # delete_index(es, index)
    # create_index(es, index)
    # s1_create_initial_doc()
    # s2_inspect_doc()
    # s3_update()
    pass
