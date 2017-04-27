#!/usr/bin/env python
# -*- coding: UTF-8 -*-
## 程序模块化,将解析www.gushequ.com的结果title和href保存到gushequ.json

__author__ = 'winsert@163.com'

import requests, random, lxml, json

from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class gushequ():
    
    def __init__(self):

        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def getUrl(self, url): 
        UA = random.choice(self.user_agent_list) #随机选出一个user_agent
        headers = {'User-Agent': UA} #构造一个完整的user-agent
        try:
            response = requests.get(url, headers=headers)
            return response
        except Exception, e:
            print 'requests：',url, '时发生以下错误：'
            print e
            sys.exit()

    def getPage(self, url):
        content = self.getUrl(url)
        pages = BeautifulSoup(content.text, 'lxml').find_all('a', class_='page-numbers') #解析出总页数
        page = pages[-2].get_text() #获得总页数
        print "共有 %r 页。" % int(page)
        return page

    def getDic(self, url):
        gsq_dic = {}
        page = self.getPage(url)
        for i in range(1, int(page)+1):
        #for i in range(1, 2): #测试提取第一页的数据
            page_url = 'http://www.gushequ.com/page/'+str(i)
            print "正在解析：", page_url
            page_content = self.getUrl(page_url)
            page_soup = BeautifulSoup(page_content.text, 'lxml').find('div', id='primary').find_all('a', rel='bookmark') # 解析page_url的内容

            for j in page_soup: #从每个page_soup中解析出title和href
                gsq_key = j['title']
                gsq_value = j['href']
                gsq_dic[gsq_key] = gsq_value

        print "共解析出 %r 条记录。" % len(gsq_dic)

        return gsq_dic #将存有title和href的字典返回

    def saveJson(self, url):
        gsq_dict = self.getDic(url)
        gj = open('gushequ.json', 'w')
        gj.write(json.dumps(gsq_dict))
        gj.close()

if __name__ == '__main__':
    
    #input_url = raw_input('请输入URL地址：')
    url = "http://www.gushequ.com"
    gsq = gushequ() #实例化
    gsq.saveJson(url)
