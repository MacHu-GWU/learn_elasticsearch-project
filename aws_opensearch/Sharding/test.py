# -*- coding: utf-8 -*-

from rich import print
from learn_elasticsearch.os_domain import es_sanhe_dev as es

index = "shard-settings-poc"

# es.indices.delete(index=index, ignore=[400, 404])
# es.indices.create(index=index, ignore=[400, 404])

res = es.indices.get_settings(index=index)
print(res)
