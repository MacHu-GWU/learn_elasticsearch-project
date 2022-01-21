Cardinality Aggregation
==============================================================================

Ref:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-cardinality-aggregation.html
- https://www.elastic.co/guide/en/elasticsearch/reference/7.16/text.html#enable-fielddata-text-fields

Cardinality 在计算机科学中的意思是 Unique 的值的数量的多少. 也就相当于 SQL 中的 ``COUNT(DISTINCT(...))``.

**Approximate**:

在 ES 中没有精确的 ``COUNT(DISTINCT(...))`` 对应实现. 在 ES 中这个值是估计值.

**Precision Threshold**:

在 aggregation query 中你可以指定 Precision Threshold. 这个值的意思是, 如果实际的 Cardinality 小于这个值, 那么结果一定是准确的, ES 会使用额外的内存来换取精确度. 而如果大于这个值, 则没法保证非常精确. 默认的 Threshold 是 3000, 最大值是 40000, 如果超过了最大值则没有意义.

**Text Field**:

Cardinality Aggregation 只能用于 Keyword 的 field, 也就是 ``{"type": "keyword"}``. 而对于 Text 的 field, 由于 ES 只保存倒排索引也就是 Token 到 _id set 的映射, 而在索引中不保存原始的值. 所以 ES 无法对 Text field 做该操作. 不过你可以在定义 mappings 的时候就定义 ``{"type": "text", "fielddata": True}``, fielddata 表示在 Index 中不但保存 _id, 还保存原始的长文本数据. 这样就可以了, 不过代价是 Index 非常消耗内存.

**Pre-computed Hash**:

对大量文本的 Field 做 Cardinality Aggregation 很耗资源, 建议在 Index 之前就自己用 Hash 算法计算 Hash 值. 该情况只适用于文本很长, 并且 Cardinality 很高的情况. 不然不划算.
