Document APIs
==============================================================================

Ref:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html

Single document APIs

- Index: Create, 插入一条新纪录, 必须要指定 _id. 如果对同一个 _id 重复插入, 则会覆盖源文档并且 version 会 +1.
- Get: Read, 根据 _id 获取文档数据.
- Update: Update, 在服务端修改数据, 免去了先 get 再 index 的 round trip. 如果非要先 get 再 index, 那么还要指定 if_seq_no, 用于防止并发修改.
- Delete: Delete, 删除数据.

Multi-document APIs

- Multi get
- Bulk
- Delete by query
- Update by query
- Reindex