#!/usr/bin/env bash

# delete index
curl -X DELETE 'http://localhost:9200/pin'

curl -X PUT 'http://localhost:9200/pin/bm/1' -d'
{
    "desc": "Lab of Genomics, Evolution, and Development at Michigan State",
    "href": "http://ged.msu.edu/",
    "tags": "ppl blog openscience python",
    "time": "2013-06-11T16:11:25Z"
}'

curl -X PUT 'http://localhost:9200/pin/bm/2' -d'
{
    "desc": "Good to Great Python reads | jesse noller",
    "href": "http://jessenoller.com/good-to-great-python-reads/",
    "tags": "python programming blog ppl",
    "time": "2013-05-15T06:46:12Z"
}'

curl -X PUT 'http://localhost:9200/pin/bm/3' -d'
{
    "desc": "Pen and Pants | Dont Leave Home Without Them",
    "href": "http://penandpants.com/",
    "tags": "blog python science teaching",
    "time": "2013-05-06T09:48:28Z"
}'

curl -X PUT 'http://localhost:9200/pin/bm/4' -d'
{
    "desc": "A Practical Intro to Data Science | Zipfian Academy",
    "href": "http://blog.zipfianacademy.com/post/46864003608/a-practical-intro-to-data-science",
    "tags": "python learning stats datamining",
    "time": "2013-04-16T14:11:41Z"
}'
