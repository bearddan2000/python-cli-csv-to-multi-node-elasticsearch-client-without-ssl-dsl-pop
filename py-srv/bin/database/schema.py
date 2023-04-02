COLUMN_NAME = {
    'col_0': {
        'name' : 'id',
        'type' : 'long'
    },
    'col_1': {
        'name' : 'name',
        'type' : 'keyword'
    },
    'col_2': {
        'name' : 'color',
        'type' : 'text'
    },
    'col_3': {
        'name': 'price',
        'type': 'double'
    },
    'col_4': {
        'name': 'quanity',
        'type': 'integer'
    }
}

configurations = {
    "settings": {
        "index": {"number_of_replicas": 2},
        "analysis": {
            "filter": {
                "ngram_filter": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 15,
                },
            },
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "ngram_filter"],
                },
            },
        },
    },
    "mappings": {
        "properties": {
            COLUMN_NAME['col_0']['name']: {
                "type": COLUMN_NAME['col_0']['type']
            },            
            COLUMN_NAME['col_1']['name']: {
                "type": COLUMN_NAME['col_1']['type'],
                "analyzer": "standard"
            },
            COLUMN_NAME['col_2']['name']: {
                "type": COLUMN_NAME['col_2']['type'],
                "analyzer": "standard"
            },
            COLUMN_NAME['col_3']['name']: {
                "type": COLUMN_NAME['col_3']['type'],
                "analyzer": "standard"
            },
            COLUMN_NAME['col_4']['name']: {
                "type": COLUMN_NAME['col_4']['type'],
                "analyzer": "standard"
            },
        }
    },
}
