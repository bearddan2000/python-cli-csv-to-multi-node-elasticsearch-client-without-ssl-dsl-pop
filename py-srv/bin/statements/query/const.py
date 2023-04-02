from elasticsearch_dsl import Search

SELECT_ALL = {"match_all": {}}

def dsl_range() -> Search:
    return Search().filter("range", id={'gt': 2})

RANGE = {
  "bool": {
    "filter": {"range": {"id": {"gt": 2}}}
  }
}

def dsl_regex() -> Search:
    return Search().query("regexp", color="red*")

REGEX = {
    "bool": {
      "must": {"regexp": { "color": "red*" }}
    }
}

def dsl_must() -> Search:
    return Search().query("match", name="Orange")

MUST = {
  "bool": {
    "must": [{"match": {"name": "Orange"}}]
  }
}

def dsl_must_filter() -> Search:
    return Search() \
      .filter("term", color="orange") \
      .query("match", name="Orange")

MUST_FILTER = {
  "bool": {
    "filter": {"term": {"color": "orange"}},
    "must": [{"match": {"name": "Orange"}}]
  }
}

def dsl_must_not_filter() -> Search:
    return Search() \
      .filter("term", color="orange") \
      .query("match", name="Orange") \
      .exclude("term", color="green")

MUST_NOT_FILTER = {
  "bool": {
    "filter": {"term": {"color": "orange"}},
    "must": [{"match": {"name": "Orange"}}],
    "must_not": [{"term": {"color": "green"}}]
  }
}

def dsl_filter() -> Search:
    return Search() \
      .filter("term", color="orange")

FILTER = {
  "bool": {
    "filter": {"term": {"color": "orange"}}
  }
}