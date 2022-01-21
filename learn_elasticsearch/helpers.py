# -*- coding: utf-8 -*-

from opensearchpy import OpenSearch


def create_index(es: OpenSearch, index: str, body: dict = None):
    # create if not exists
    return es.indices.create(index=index, body=body, ignore=400)


def delete_index(es: OpenSearch, index: str):
    # delete if exists
    return es.indices.delete(index=index, ignore=[400, 404])


def reset_index(es: OpenSearch, index: str, body: dict = None):
    delete_index(es, index)
    create_index(es, index, body)
