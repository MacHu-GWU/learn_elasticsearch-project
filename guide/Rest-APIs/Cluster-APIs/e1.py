# -*- coding: utf-8 -*-

from rich import print
from learn_elasticsearch.os_domain import es_sanhe_dev as es

#--- Get cluster stats
res = es.cluster.stats()
# print(res)

#--- Get all nodes info
# info 是 node 上的配置信息, 也包含部分统计数据
res = es.nodes.info()
# print(res)

#--- Get all nodes stats
# stats 主要是统计数据
res = es.nodes.stats()
# print(res)

#--- Get all nodes usage
# 主要是资源占用信息
res = es.nodes.usage()
# print(res)