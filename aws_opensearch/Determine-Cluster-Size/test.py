# -*- coding: utf-8 -*-

import faker
import random
from rich import print
from opensearchpy.helpers import bulk
from learn_elasticsearch.os_domain import es_sanhe_dev as es

index = "determine_cluster_size_test"

fake = faker.Faker()

def gen_customer(fake):
    dob = fake.date_of_birth()
    dct = {
        "customer_firstname": fake.first_name(),
        "customer_lastname": fake.last_name(),
        # "": fake.address(),
        "customer_street": fake.street_address(),
        "customer_city": fake.city(),
        "customer_state": fake.state(),
        "customer_postcode": fake.postcode(),
        "customer_telephone": fake.phone_number(),
        "customer_dob": str(dob),
        "customer_dob_year": dob.year,
        "customer_dob_month": dob.month,
        "customer_dob_day": dob.day,
    }
    dct["customer_address"] = "{}, {}, {} {}".format(
        dct["customer_street"],
        dct["customer_city"],
        dct["customer_state"],
        dct["customer_postcode"],
    )
    return dct


def gen_data(index, fake):
    n_customer = 1_000
    _index = "_index"
    _id = "_id"
    _source = "_source"
    for id in range(1, n_customer + 1):
        print(id)
        dct = gen_customer(fake)
        dct["customer_id"] = id
        return {
            _index: index,
            _id: id,
            _source: dct
        }



# print(gen_customer(fake))
# es.indices.delete(index=index, ignore=[400, 404])
# es.indices.create(index=index, ignore=[400,])
# bulk(es, gen_data(index=index, fake=fake))
