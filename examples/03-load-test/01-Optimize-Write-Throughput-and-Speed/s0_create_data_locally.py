# -*- coding: utf-8 -*-

"""
在本地创建 100 个 JSON 文件, 每个 JSON 文件由 100,000 条数据. 一共 10M 条数据.
总计体积 8.8G 左右.
"""

import json
import random
import mpire
import faker
import uuid
from rich import print
from pathlib_mate import Path

categories = [
    "Politics", "Military", "Education", "Finance", "Technology",
    "Sport", "Entertainment", "Movie", "TV", "Science",
]

def create_document(id: int, fake: faker.Faker) -> dict:
    return {
        "news_id": id,
        "url": str(uuid.uuid4()),
        "create_date": str(fake.date()),
        "author": fake.name(),
        "summary": fake.paragraph(nb_sentences=20),
        "category": random.choice(categories)
    }


def test_create_document():
    fake = faker.Faker()
    doc = create_document(id=1, fake=fake)
    print(doc)


def create_one_file(
    nth: int,
    start_id: int,
    n_records: int,
    fake: faker.Faker,
):
    dir_here = Path(__file__).parent
    file = Path(dir_here, "data1", "{}.json".format(str(nth).zfill(6)))
    print(f"create file at {file.basename}")
    data = [
        create_document(id, fake)
        for id in range(start_id, start_id + n_records)
    ]
    file.write_text(json.dumps(data))


def create_many_file(
    start_nth: int,
    n_file: int,
    n_records_per_file: int,
    fake: faker.Faker,
):
    for i in range(n_file):
        nth = start_nth + i
        start_id = 1 + n_records_per_file * (nth - 1)
        create_one_file(nth, start_id, n_records_per_file, fake)


def multiprocess_create_many_file(fake: faker.Faker):
    with mpire.WorkerPool(n_jobs=4, start_method="spawn") as pool:
        pool.map(
            create_many_file,
            [
                (1, 25, 100_000, fake),
                (26, 25, 100_000, fake),
                (51, 25, 100_000, fake),
                (76, 25, 100_000, fake),
            ],
        )

if __name__ == "__main__":
    # test_create_document()
    fake = faker.Faker()
    # create_one_file(nth=1, start_id=1, n_records=100, fake=fake)
    # create_many_file(start_nth=76, n_file=25, n_records_per_file=100_000, fake=fake)
    # multiprocess_create_many_file(fake=fake)

    pass

