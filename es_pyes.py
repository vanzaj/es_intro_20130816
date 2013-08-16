from pyelasticsearch import ElasticSearch
from pprint import pprint

es = ElasticSearch('http://localhost:9200/')

pprint(es.get('pin','bm', 1))

pprint(es.search('tags:blog', size=2, index='pin'))
pprint(es.search('tags:blog AND genomics', index='pin'))

