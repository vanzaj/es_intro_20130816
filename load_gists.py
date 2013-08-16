#!/usr/bin/env python

import requests as req
import json
from pprint import pprint

def filter_gists(data):
    fields = ('id', 'user', 'created_at', 'url', 'description', 'files')
    resu = list()
    for item in data:
        gist = dict()
        for field in fields:
            gist[field] = item.get(field, 'empty')
        resu.append(gist)
    return resu


#url = 'https://api.github.com/gists/public'
#rsp = req.get(url)
#gists = rsp.json()
gists = json.load(open('data_gists.json', 'r'))

limit = 10
n_gists = len(gists)
cut = limit if n_gists > limit else n_gists
print "Nb of gists: %d" % n_gists
print "Nb of gists to send to ES: %d" % cut


gists = filter_gists(gists[:cut])

es_host = 'http://localhost:9200'
es_idx = 'gists'
es_type = 'g'

# reset index
url = "%s/%s" % (es_host, es_idx)
rsp = req.delete(url)
if rsp.ok:
    print "%s index reset" % es_idx 

for i,gist in enumerate(gists):
    _id = i+1
    url = "%s/%s/%s/%d" % (es_host, es_idx, es_type, _id)
    rsp = req.put(url, data=json.dumps(gist))
    if rsp.ok:
        print "%s -> id: %d" % (gist['url'], _id)

