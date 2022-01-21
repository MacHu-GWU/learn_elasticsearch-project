# -*- coding: utf-8 -*-

"""
测试 Fuzzy Search 的性能.

如果在还有其他过滤条件的情况下, 例如 term query 能 filter 掉一大半结果, 那么查询引擎会优先
执行 term 使得 fuzzy match 的 scope 变小, 从而提高性能.
"""

from rich import print
import faker
from opensearchpy.helpers import bulk
from learn_elasticsearch.os_domain import es_sanhe_dev as es

index = "fuzzy_query"


def s01_delete_index():
    es.indices.delete(index=index, ignore=[400, 404])


def s02_create_index():
    body = {
        "mappings": {
            "properties": {
                "city": {"type": "text"},
                "state": {"type": "keyword"},
            }
        }
    }
    es.indices.create(index=index, body=body, ignore=[400, 404])


def s03_delete_data():
    body = {"query": {"match_all": {}}}
    res = es.delete_by_query(index=index, body=body)
    print(res)


def s04_prepare_data():
    n_doc = 1000
    fake = faker.Faker()
    actions = [
        {
            "_index": index,
            "_id": i,
            "_source": {
                "city": fake.city(),
                "state": fake.state(),
            }
        }
        for i in range(1, 1 + n_doc)
    ]
    states = [action["_source"]["state"] for action in actions]
    counts = dict()
    for state in states:
        try:
            counts[state] += 1
        except:
            counts[state] = 1
    print(counts)
    res = bulk(es, actions)
    print(res)


def s05_get_test_doc(id):
    res = es.get(index=index, id=id)
    print(res)


def s06_count_by_state():
    body = {
        "aggs": {
            "state": {
                "terms": {"field": "state", "size": 1000}
            }
        }
    }
    res = es.search(index=index, body=body)
    print(res)


def s07_fuzzy_search_performance_test():
    # This style is not recommended and only support in ES, not support in OpenSearch
    # body = {
    #     "query": {
    #         "fuzzy": {
    #             "city": {
    #                 "value": "Pirt Kevon",
    #                 "fuzziness": 1,
    #             }
    #         }
    #     },
    # }

    body1 = {
        # "profile": True,
        "query": {
            "match": {
                "city": {
                    "query": "East Michael",
                    "fuzziness": 70,
                }
            }
        },
    }

    body2 = {
        # "profile": True,
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "city": {
                                "query": "East Michelletown",
                                "fuzziness": 70,
                            },
                        },
                    },
                    {
                        "term": {
                            "state": "Oregon",
                        },
                    },
                ],
            },
        },
    }
    res = es.search(index=index, body=body1)
    print(res)


def s08_fuzzy_search_on_different_field_test():
    """
    Fuzzy search 可以用作 text 或是 keyword 的 field.
    """
    body = {
        "query": {
            "match": {
                # "city": {
                #     "query": "Traceyfurt",
                #     "fuzziness": 70,
                # },
                "state": {
                    "query": "Mississippi",
                    "fuzziness": 70,
                }
            }
        },
    }
    res = es.search(index=index, body=body)
    print(res)


if __name__ == "__main__":
    """
{
    'Maine': 20034,
    'South Carolina': 20130,
    'Arkansas': 19967,
    'Alabama': 19911,
    'Texas': 20050,
    'Georgia': 19945,
    'Delaware': 20079,
    'New Hampshire': 20124,
    'North Carolina': 19980,
    'Idaho': 20036,
    'Washington': 20392,
    'South Dakota': 19984,
    'Florida': 20018,
    'New Jersey': 20174,
    'Arizona': 19883,
    'Missouri': 19866,
    'Montana': 19828,
    'West Virginia': 19930,
    'North Dakota': 20019,
    'Kansas': 19984,
    'Oklahoma': 19815,
    'Michigan': 19846,
    'New York': 19865,
    'Hawaii': 19881,
    'Vermont': 20095,
    'Utah': 20115,
    'Maryland': 20065,
    'Nebraska': 20051,
    'Nevada': 19820,
    'Connecticut': 19974,
    'Alaska': 19958,
    'Oregon': 20153,
    'Louisiana': 20086,
    'California': 19842,
    'Ohio': 19906,
    'Kentucky': 20126,
    'Virginia': 19906,
    'New Mexico': 19937,
    'Rhode Island': 20056,
    'Mississippi': 19823,
    'Wisconsin': 20384,
    'Massachusetts': 19642,
    'Iowa': 19868,
    'Illinois': 20064,
    'Minnesota': 19898,
    'Indiana': 20326,
    'Tennessee': 19950,
    'Pennsylvania': 19995,
    'Colorado': 20205,
    'Wyoming': 20014
}
    """
    # s01_delete_index()
    # s02_create_index()
    # s03_delete_data()
    # s04_prepare_data()
    # s05_get_test_doc(id=764)
    # s06_count_by_state()
    # s07_fuzzy_search_performance_test()
    # s08_fuzzy_search_on_different_field_test()
    pass
