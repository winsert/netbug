#!/usr/bin/env python
# -*- coding: UTF-8 -*-
## 对soup.txt进行步步解析

import requests
from bs4 import BeautifulSoup
import os
 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sp = open('./soup.txt', 'r')

result = BeautifulSoup(sp.read(), 'lxml').find('div', class_="rich_media_content ")

print result.get_text()

'''
for i in result:
    #print i, '\n'
    print i['title']
    print i['href']

#print '找到:', result
'''
sp.close()
