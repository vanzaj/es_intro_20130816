from __future__ import print_function
import pprint
import json
import requests as req

host = 'http://localhost:9200'


def es(ep, pars=None, data=None, host=host, method='get'):
    url = '%s/%s' % (host.rstrip('/'), ep.strip('/'))
    method = method.lower()
    if method == 'head':
        r = r.head(url)
    elif method == 'post':
        r = req.post(url, params=pars, data=pars)
    elif method == 'put':
        r = req.put(url, params=pars, data=pars)
    elif method == 'delete':
        r = req.delete(url)
    else:
        r = req.get(url, params=pars, data=data)
    return r

def print_r(r):
    pp = pprint.PrettyPrinter(stream=None, indent=1, width=80, depth=None)
    print(r.request.method, r.url)
    pp.pprint(r.json())
    print('='*42)



if __name__ == '__main__':
    # GET by ID'
    r = es('/pin/bm/1')
    print_r(r)

    # basic search
    r = es('/pin/_search?q=blog')
    print_r(r)

    # basic search with a limit
    p = {'q': 'blog', 'size': 2}
    r = es('/pin/_search', pars=p)
    print_r(r)

    # search using query dsl
    d = {
          "query": {
            "query_string": {
              "query": "blog", 
              "fields": ["tags"] 
             } 
          }
        }
    dj = json.dumps(d)
    r = es('/pin/_search', data=dj, method='post')
    print_r(r)

