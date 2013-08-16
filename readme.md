Notes on quick into to ES at Friday Tech Talks @ Blk71 (Fri, Aug 16, 2013)

Quick start
===========

Install, launch, test:

     brew install elasticsearch
     elasticsearch -f
     curl 'localhost:9200'  # or via browser

Load some data:

     ./load_pinbrd.sh

get docs by id:

     curl 'localhost:9200/pin/bm/1'
     curl 'localhost:9200/pin/bm/1?pretty'
     curl 'localhost:9200/pin/bm/1?format=yaml'

ElasticSearch urls have the following structure: 
``host[/index][/mapping_type][/id][/method]``. In ES speak, `index` ~ database name,
`type` ~ schema, `id` ~ record id. Some examples of methods: `_search`,
`_mapping`, `_analyze`, `_status`.



Basic Search
============

Download
[Sense](https://chrome.google.com/webstore/detail/sense/doinijnbnggojdlcjifpdckfokbbfpbo?hl=en)
 extension

::

     /pin/bm/_search?q=science
     /pin/_search?q=tags:*science
     /pin/_search?q=tags:*science&size=2

::

     ./load_gists.py

::

     /_search?q=description:python || desc:python
     curl 'http://localhost:9200/pin/_search?q=tags:python%20AND%20blog'


Access with Python
==================

::

     python es_req.py    # using requests
     python es_pyes.py   # using pyelasticsearch



Search DSL
----------

Query:

    { 
      "query": { 
        "match_all" : {} 
      } 
    }


    {
      "query": {
        "query_string": {
            "query": "blog",
            "fields": ["tags"]
        }
      }
    }


Highlighting:

    {
      "query": {
        "query_string": {
            "query": "genomics"
        }
      },
      "highlight": {
        "fields": {
          "desc": {}
        }
      }
    }

Facets:

    {
      "query": {
        "match_all" : {}
      },
      "facets" : {
        "tags" : {
            "terms" : { "field" : "tags" }
        }
      }
    }


Other stuff
===========

::

    curl 'localhost:9200/_analyze?analyzer=standard&pretty' -d 'hello world'
    curl 'localhost:9200/_analyze?analyzer=whitespace&pretty' -d 'hello world'
    curl 'localhost:9200/pin/_stats?pretty'

    curl 'http://localhost:9200/_aliases?pretty'
    curl 'http://localhost:9200/_status?pretty'
    curl 'http://localhost:9200/_cluster/nodes/stats?pretty'
