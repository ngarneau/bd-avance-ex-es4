import json
import elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import Match, MultiMatch

es = elasticsearch.Elasticsearch()
INDEX = "bd_avance"
DOC_TYPE = "restaurants"


def get_data(fname):
    with open(fname) as fhandle:
        for line in fhandle:
            filtered_data = {}
            data = json.loads(line, encoding='utf-8')
            filtered_data["id"] = data["restaurant_id"]  # Remapping the id for ES
            filtered_data["name"] = data["name"]
            filtered_data["coord"] = data["address"]["coord"]
            filtered_data["cuisine"] = data["cuisine"]
            yield filtered_data


def index_restaurants(emails):
    for e in emails:
        es.index(
            INDEX,
            DOC_TYPE,
            body=e,
            id=e['id']
        )

# 1.1
def bounding_time_square():
    pass

# 1.2
def polygon():
    pass

# 1.3
def polygon_american():
    pass


# 1.4
def rockefeller_2KM():
    pass


# 1.5
def rockefeller_2KM_chinese():
    pass


# 1.6
def aggregate():
    pass


# 2.2
def index_objects():
    pass


# 2.3
def find_in_time_square():
    pass


# 2.4
def find_out_time_square():
    pass


# 2.5
def find_through_time_square():
    pass


# 2.6
def find_time_square_contains():
    pass


if __name__ == '__main__':
    pass