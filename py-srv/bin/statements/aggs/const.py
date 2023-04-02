from elasticsearch_dsl import Search

aggs = [
    '_avg', '_count', '_max',
    '_min', '_sum', '_distinct_count',
    '_all_stats', '_stats'
]

all_stats_subkey = [
    'count', 'sum', 'avg', 
    'min', 'max', "sum_of_squares", 
    "variance", "std_deviation"
]

def dsl_average(s: Search) -> Search:
    s.aggs.metric('_avg', 'avg', field='price')
    return s

AVG_AGGR = {
  "_avg": {
    "avg": {"field": "price" }
  }
}

def dsl_count(s: Search) -> Search:
    s.aggs.metric('_count', 'value_count', field='id')
    return s

COUNT_AGGR = {
  "_count": {
    "value_count": {"field": "id" }
  }
}

def dsl_max(s: Search) -> Search:
    s.aggs.metric('_max', 'max', field='price')
    return s

MAX_AGGR = {
  "_max": {
    "max": {"field": "price" }
  }
}

def dsl_min(s: Search) -> Search:
    s.aggs.metric('_min', 'min', field='price')
    return s

MIN_AGGR = {
  "_min": {
    "min": {"field": "price" }
  }
}

def dsl_sum(s: Search) -> Search:
    s.aggs.metric('_sum', 'sum', field='price')
    return s

SUM_AGGR = {
  "_sum": {
    "sum": {"field": "price" }
  }
}

def dsl_distinct_count(s: Search) -> Search:
    s.aggs.metric('_distinct_count', 'cardinality', field='price')
    return s

DISTINCT_AGGR = {
    "_distinct_count":{
      "cardinality":{"field":"price"}
    }
}

def dsl_stats(s: Search) -> Search:
    s.aggs.metric('_stats', 'stats', field='price')
    return s

STATS_AGGR = {
    "_stats" : { "stats" : { "field" : "price" } }
}

def dsl_all_stats(s: Search) -> Search:
    s.aggs.metric('_all_stats', 'extended_stats', field='price')
    return s

ALL_STATS_AGGR = {
    "_all_stats" : { "extended_stats" : { "field" : "price" } }
}