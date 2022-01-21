Index APIs
==============================================================================

.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:

Ref:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/indices.html

Summary
------------------------------------------------------------------------------

**Index management**

- Create index: 创建
- Delete index: 删除
- Get index: 获得 metadata 信息
- Exists: 检查是否存在
- Close index: 临时关闭以节约内存
- Open index: 重新打开
- Shrink index: 为一个已经存在的 Index 创建一个新的替代 Index, 数据一致, 但是 Primary Shard 数量更少. 该操作要求 Index 是 Read Only 状态, 所有的 Primary Shard 在同一个 Node 上, index 必须处于 green health status.
- Split index: 为一个已经存在的 Index 创建一个新的替代 Index, 数据一致, 但是 Primary Shard 数量更多. 该操作要求 Index 是 Read Only 状态, index 必须处于 green health status.
- Clone index: 为一个已经存在的 Index 创建一个一摸一样的新的替代 Index. 该操作要求 Index 是 Read Only 状态, index 必须处于 green health status.
- Rollover: 是 ES 处理冷热数据和时间序列数据的方式. 你希望活跃索引尽量分部到多的节点上, 对于冷数据你想要减少分片以减少资源占用. `参考资料 <https://www.elastic.co/blog/managing-time-based-indices-efficiently>`_
- Freeze index:
- Unfreeze index:
- Resolve index:

**Mapping management**

- Update mapping:
- Get mapping:
- Get field mapping:
- Type exists:
- Analyze index disk usage:

**Alias management**

- Aliases:
- Create or update alias:
- Get alias:
- Alias exists:
- Delete alias:

**Index settings**

- Update index settings:
- Get index settings:
- Analyze:

关于 Open / Close, Freeze / Unfreeze, Snapshot / Restore
------------------------------------------------------------------------------
维持一个 Index 出于 Open for search 的状态是需要很多 Memory 的. 一个很常见的需求是: 一个 Index 暂时不需要, 所以想暂时让这个 Index 不占用服务器性能, 但又想保留数据, 等以后要用的时候能尽快恢复. ES 提供了多种办法解决这一问题.

1. Close: 关闭一个 Index, 关闭后就不占用内存资源了, 同时也不再接受 Read / Write 的请求. 当你重新 Open 的时候, 会自动进入 restore 的流程, 这个 Open 不是瞬时的. 要注意的是, Close 以后, 数据仍然留在 Shard 上, 但同一个 Shard 可能还在服务于其他 Index. 所以这个 Shard 是有可能挂掉并且被替换掉的. 对于处于 Open 状态的 Index, 这个 Shard 被替换后数据会被自动从 Replica 上迁徙. 而对于处于 Close 状态的 Index, 数据是不会被自动迁徙的. 所以是有丢数据的风险的. 所以 Close 一个 Index 的时间不能太长.
2. Freeze: 冻结一个 Index. 一旦被冻结, 内存中的数据将会被持久化到硬盘上, 并且变为只读, 并且用于 search 的 heap 堆数据也会被持久化到硬盘上, 并且占用大量硬盘. 期间依然可以接受 search request, 但是并发数量责备限制为 1. 被 Freeze 后的 Index 的可以被 Unfreeze. (注意 7.14 以后好像 Freeze / Unfreeze 不再有意义了)
3. Snapshot: 和其他数据库备份技术很像, 是整个数据库磁盘的一个快照, 可以储存在 AWS S3 之类的云存储上. Restore 则是从 Snapshot 中恢复数据.
