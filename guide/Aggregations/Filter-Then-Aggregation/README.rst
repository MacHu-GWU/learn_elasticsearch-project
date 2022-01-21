Filter Then Aggregation
==============================================================================
在 SQL 中我们常常会用 WHERE 先对数据进行 Filter. 然后对 Filter 的结果进行 Group By 之类的 Aggregation 统计. 在 ElasticSearch 中也有对应的语法::

    {
        "query": {
            ...
        }, # 如果是多个条件则可以用 "bool": {...}
        "agg": {
            ...
        }
    }
