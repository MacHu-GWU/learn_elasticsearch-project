Determine Cluster Size (如何确定需要多少 Node 和 Shard)
==============================================================================

Keyword:

- How many node / instance do I need?
- How many shard do I need?

Reference:

- https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html
- https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-how-many-data-instances-do-i-need/
- https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-how-many-shards-do-i-need/

Calculate Storage Requirement
------------------------------------------------------------------------------
你要了解的信息:

1. Number of replicas: 默认设置是有一个 replica 的. 也就是说假设你不用 replica 存储是 1G, 那么总共需要 2G 空间. 更多的replica 能增加你 read 的性能.
2. OpenSearch indexing overhead: index 实际占据的磁盘空间要比 ES 的统计值, 或是你手动插入和的测量值要多 10%.
3. Operating system reserved space: 操作系统需要预留大约 5% 的磁盘空间
4. OpenSearch Service overhead: ES 需要 20% 的磁盘空间用于 segment, merge, logs 等其他操作时的临时空间. 这个值不会操作 20GB.

你可以先启用一个 dev / test 的 domain, 然后只用 1 个 node. 比如你的数据有 1000,000,000 条. 你可以手动插入大约比较有代表性的 1000,000 条数据. 然后用 


1. 首先你需要测算你的 Index 需要占用多少空间. 你可以先创建一个单个 Node 的 Instance, 然后配置好 Mapping, 再把数据写入 Index. 然后用 ``client.indices.stats(index=index)`` API 获得磁盘大小. 设这个值为 X.
2. X * (1 + Number of Replicas) * (1 + Indexing Overhead ~ 0.1) / (1 - Linux Reserved Space ~ 0.05) / (1 - OpenSearch Service Overhead ~ 0.2) = Minimum Storage Requirement. 简单来说你可以用 X * (1 + Number of Replicas) * 1.45 来简化计算.
