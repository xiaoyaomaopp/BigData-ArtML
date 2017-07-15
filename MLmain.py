# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:14:53 2016

@author: Administrator
"""
#数据库中读取数据
import mongodb.pymongo_class as mongdb_class
import data.wiki.wiki_author as wiki_author_class
import pandas as pd       

ip = '10.82.0.1';
port = 27017;
dataBase = 'crawlerNew';    
author_wiki = mongdb_class.MongoClass(ip,port,dataBase,'wikiart.org.author');
authorList_wiki = author_wiki.find_mongo({});
art_wiki = mongdb_class.MongoClass(ip,port,dataBase,'wikiart.org.art');
artList_wiki = art_wiki.find_mongo({});

#数据模型转换
docsAuthor_list  = pd.DataFrame(authorList_wiki);
docsArt_list = pd.DataFrame(artList_wiki);
docsAuthor_list = docsAuthor_list.where(docsAuthor_list.notnull(), None)
docsArt_list = docsArt_list.where(docsArt_list.notnull(), None)

#清理wiki作者字段
wiki_author = wiki_author_class.wiki_author(docsAuthor_list,ip,port,dataBase);