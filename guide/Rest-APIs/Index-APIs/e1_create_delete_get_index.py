# -*- coding: utf-8 -*-

from rich import print
from learn_elasticsearch.os_domain import es_sanhe_dev as es

index = "guide_rest_apis_index_apis"


def create_get_exists_delete_index():
    # --- Check if index exists
    res = es.indices.exists(index=index)
    # print(res)

    # --- Create index if not exists
    # ignore 400 cause by resource_already_exists_exception when creating an index
    res = es.indices.create(index=index, ignore=400)
    # print(res)

    # --- Get index metadata
    res = es.indices.get(index=index)
    # print(res)

    # --- Delete index if exists
    # ignore 404 and 400 cause by index_not_found_exception when deleting an index
    res = es.indices.delete(index=index, ignore=[400, 404])
    # print(res)


def get_and_update_index_settings():
    res = es.indices.create(index=index, ignore=400)

    # check before state
    res = es.indices.get_settings(index=index)
    print(res)

    # --- Update index settings
    # 具体的参数和选项可以参考 https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html#index-modules-settings
    # 很多操作都需要将 index 先 close, 再 update 然后重新 open
    res = es.indices.put_settings(
        index=index,
        body={
            "number_of_replicas": 1,
            "number_of_routing_shards": 10,
        },
    )
    print(res)

    # check after state
    res = es.indices.get_settings(index=index)
    print(res)
