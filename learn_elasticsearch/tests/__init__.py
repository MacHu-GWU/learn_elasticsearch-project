# -*- coding: utf-8 -*-

from opensearchpy import OpenSearch
from ..os_domain import (
    boto_ses,
    es_sanhe_dev,
)


def create_index(es: OpenSearch, index: str, body: dict = None):
    # create if exists
    es.indices.create(index=index, ignore=400, body=body)


def delete_index(es: OpenSearch, index: str):
    # delete if exists
    es.indices.delete(index=index, ignore=[400, 404])


def reset_index(es: OpenSearch, index: str, body: dict):
    delete_index(es, index)
    create_index(es, index, body)
