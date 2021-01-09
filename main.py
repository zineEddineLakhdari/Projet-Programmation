#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 02:15:39 2021

@author: ZineEddine
"""
 


################################## Déclaration des classes ##################################

import datetime as dt
import re

import pickle

from Corpus import Corpus
from Author import Author
from Class_Document import Document

import praw

import urllib.request
import xmltodict   



################################## Création du Corpus ##################################

corpus = Corpus("Corona")


reddit = praw.Reddit(client_id='A7Cy6zC5PKFqoQ', client_secret='nLLooEBnPAnYNP2yonryN_97foY', user_agent='Reddit WebScraping')
hot_posts = reddit.subreddit('Coronavirus').hot(limit=100)
for post in hot_posts:
    datet = dt.datetime.fromtimestamp(post.created)
    txt = post.title + ". "+ post.selftext
    txt = txt.replace('\n', ' ')
    txt = txt.replace('\r', ' ')
    doc = Document(datet,
                   post.title,
                   post.author_fullname,
                   txt,
                   post.url)
    corpus.add_doc(doc)

url = 'http://export.arxiv.org/api/query?search_query=all:covid&start=0&max_results=100'
data =  urllib.request.urlopen(url).read().decode()
docs = xmltodict.parse(data)['feed']['entry']

for i in docs:
    datet = dt.datetime.strptime(i['published'], '%Y-%m-%dT%H:%M:%SZ')
    try:
        author = [aut['name'] for aut in i['author']][0]
    except:
        author = i['author']['name']
    txt = i['title']+ ". " + i['summary']
    txt = txt.replace('\n', ' ')
    txt = txt.replace('\r', ' ')
     
    doc = Document(datet,
                   i['title'],
                   author,
                   txt,
                   i['id']
                   )
    corpus.add_doc(doc)
 
#Chercher dans le corpus le mot passer en paramètre 
#Affichage des lignes ou le mot est apparue

corpus.search("covid-19")









