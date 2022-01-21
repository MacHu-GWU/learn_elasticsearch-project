# -*- coding: utf-8 -*-

from .connection import create_connection
from .boto_ses import boto_ses

es_sanhe_dev = create_connection(
    boto_ses=boto_ses,
    aws_region="us-east-1",
    es_endpoint="https://search-sanhe-dev-ce5xh5zovkiwjkf2x4c4k2saf4.us-east-1.es.amazonaws.com",
    test=False,
)

es_sanhe_prod = create_connection(
    boto_ses=boto_ses,
    aws_region="us-east-1",
    es_endpoint="https://search-sanhe-prod-jzvar2nbpbv3dne4sm7ho6crva.us-east-1.es.amazonaws.com",
    test=False,
)

es_write_throughput_test_1 = create_connection(
    boto_ses=boto_ses,
    aws_region="us-east-1",
    es_endpoint="https://search-write-throughput-test-1-y5ed5yp6uc4pmycwi3b4m6cwbq.us-east-1.es.amazonaws.com",
    test=False,
)

es_write_throughput_test_2 = create_connection(
    boto_ses=boto_ses,
    aws_region="us-east-1",
    es_endpoint="https://search-write-throughput-test-2-edyncuhofzqcam7ipkmbeuqr6m.us-east-1.es.amazonaws.com",
    test=False,
)
