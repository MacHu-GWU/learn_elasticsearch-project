所谓 Aggregation 就是聚合查询. 例如统计数量, 计算平均值, 按照值分桶等等. ES 支持以下三种聚合查询:

- Metric: aggregations that calculate metrics, such as a sum or average, from field values.
- Bucket: aggregations that group documents into buckets, also called bins, based on field values, ranges, or other criteria.
- Pipeline: aggregations that take input from other aggregations instead of documents or fields.
