Primary Shard and Replica Shard
------------------------------------------------------------------------------

The primary shard receives all writes first. It passes new documents off to all replicas for indexing. By default, it then waits for the replicas to acknowledge the write before returning success to the caller. The primary and a replica shard are redundant storage for the data, hardening the cluster to the loss of an instance.

