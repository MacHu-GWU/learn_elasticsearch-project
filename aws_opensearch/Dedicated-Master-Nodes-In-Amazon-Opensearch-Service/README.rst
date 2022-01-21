Dedicated master nodes in Amazon OpenSearch Service
==============================================================================

Ref:

- https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html

Dedicated Master Node 是一个只用于 Management 的 Node, 并不储存任何数据. 该 Node 能进行一些自动检查 Data Node 存活, 启动新的 Data Node, 迁徙数据等一系列工作.

在 AWS 的最佳实践中, Prod 环境里的 Master Node 必须是奇数, 否则在有 Node 挂掉后无法用 quorum 选举算法选出该使用哪个 Master Node 中的 backup 作为新的 Master Node.

简单来说: 3, 5, 7 都可以. 3 用的最多, 能允许一个 node 挂掉. 5 也不错, 能允许两个 node 挂掉.

Dedicated Master Node 会做以下工作:

- Track all nodes in the cluster
- Track the number of indices in the cluster
- Track the number of shards belonging to each index
- Maintain routing information for nodes in the cluster
- Update the cluster state after state changes, such as creating an index and adding or removing nodes in the cluster
- Replicate changes to the cluster state across all nodes in the cluster
- Monitor the health of all cluster nodes by sending heartbeat signals, periodic signals that monitor the availability of the data nodes in the cluster

由于 Master Node 要管理你的 Index 和 Shard. 所以 Index 越大, Data Node 越多, 你的 Master Node 的配置也要越强. 你可以参考下表::

    +----------------+----------------------------------------------------+
    | Instance count | Recommended minimum dedicated master instance type |
    +----------------+----------------------------------------------------+
    |      1–10      |         m5.large.search or m6g.large.search        |
    +----------------+----------------------------------------------------+
    |      10–30     |        c5.xlarge.search or c6g.xlarge.search       |
    +----------------+----------------------------------------------------+
    |      30–75     |       c5.2xlarge.search or c6g.2xlarge.search      |
    +----------------+----------------------------------------------------+
    |     75–200     |       r5.4xlarge.search or r6g.4xlarge.search      |
    +----------------+----------------------------------------------------+
