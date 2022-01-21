# -*- coding: utf-8 -*-

"""
对于单个文档的:

- insert
- get
- update
- delete
"""

import base64
from rich import print
from learn_elasticsearch.os_domain import es_sanhe_dev as es

index = "crud_examples"


def serialize_binary(b) -> str:
    return base64.b64encode(b).decode("utf-8")


def deserialize_binary(s) -> bytes:
    return base64.b64decode(s.encode("utf-8"))


def reset_index():
    # delete if exists
    es.indices.delete(index=index, ignore=[400, 404])
    # create if exists
    es.indices.create(index=index, ignore=400)


def single_document_crud():
    """
    Ref: https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html

    - Create = index
    - Read = get
    - Update = update
    - Delete = delete
    """
    # --- index
    body = {
        "id": 1,
        "a_int": 1,
        "a_float": 3.14,
        "a_str": "this is string",
        "a_bytes": serialize_binary("this is bytes".encode("utf-8")),
    }
    res = es.index(index=index, id=1, body=body)
    print("--- index response")
    # print(res)

    # --- get
    print("--- get response")
    res = es.get(index=index, id=1)
    # print(res)

    # --- update
    update_body = {
        "script": {
            "source": "ctx._source.a_float = params.a_float",
            "lang": "painless",
            "params": {
                "a_float": 2.72
            }
        }
    }
    res = es.update(index=index, id=1, body=update_body)
    print("--- update response")
    # print(res)

    # --- delete
    res = es.delete(index=index, id=1)
    print("--- delete response")
    # print(res)

    res = es.get(index=index, id=1, ignore=[400, 404])
    print("--- get response")
    print(res)


# reset_index()
# single_document_crud()


def qa_index_full_replacement_or_not():
    """
    问题: insert 一条 documents, _id 已经存在, 是否会 raise 异常? 是否是全部覆盖? 还是只
    覆盖部分 fields. 版本号是否会增加?

    结论: 不会 raise 异常, 是全量覆盖, version 会 + 1
    """
    id_ = "test_index_full_replacement_or_not"
    res = es.index(index=index, id=id_, body={"name": "alice", "email": "alice@google.com"})
    print(res)

    res = es.get(index=index, id=id_)
    print("--- get response")
    print(res)

    res = es.index(index=index, id=id_, body={"email": "alice@outlook.com"})
    print(res)

    res = es.get(index=index, id=id_)
    print("--- get response")
    print(res)


# qa_index_full_replacement_or_not()

def qa_upsert_or_not():
    """
    问题: update 一条 documents, _id 并不存在, 会不会自动 insert?

    结论: _id 如果不存在则不会 insert.
    """
    id_ = "test_upsert_or_not"

    res = es.delete(index=index, id=id_, ignore=[404])
    print(res)

    update_body = {
        "script": {
            "source": "ctx._source.a_int = 99",
            "lang": "painless",
        }
    }
    res = es.update(index=index, id=id_, body=update_body)
    print(res)


qa_upsert_or_not()


def qa_update_increase_version_or_not():
    """
    问题: update 一条 documents, _id 已经存在, 版本号是否会增加?

    结论: version 会 + 1
    """
    id_ = "test_update_increase_version_or_not"

    res = es.index(index=index, id=id_, body={"count": 0})
    # print(res)

    res = es.get(index=index, id=id_)
    print("--- get response")
    print(res)

    update_body = {
        "script": {
            "source": "ctx._source.count = params.increment",
            "lang": "painless",
            "params": {
                "increment": 1
            }
        }
    }
    res = es.update(index=index, id=id_, body=update_body)
    # print(res)

    res = es.get(index=index, id=id_)
    print("--- get response")
    print(res)


# qa_update_increase_version_or_not()


def qa_delete_reset_version_or_not():
    """
    问题: delete 一条 document 之后, 是否会 reset version 到 0?

    结论: 不会
    """
    id_ = "test_delete_reset_version_or_not"
    es.index(index=index, id=id_, body={"name": "alice"})
    es.index(index=index, id=id_, body={"name": "bob"})
    res = es.get(index=index, id=id_)
    print(res)

    es.delete(index=index, id=id_)
    es.index(index=index, id=id_, body={"name": "cathy"})
    res = es.get(index=index, id=id_)
    print(res)

# qa_delete_reset_version_or_not()
