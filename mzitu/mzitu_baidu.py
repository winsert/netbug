#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'winsert@163.com'

import requests
from bs4 import BeautifulSoup
import os
 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class mzitu():

    def get_name(self, url):
        html = self.request(url) ##调用request函数把套图地址传进去,返回一个response
        page_name = BeautifulSoup(html.text, 'lxml').find('title').get_text()
        self.mkdir(page_name)  ##调用mkdir函数创建文件夹
        self.html(url) ##调用html函数把url参数传递过去
        self.up() ##调用up函数把下载的图片文件夹上传到百度云

    def html(self, url):   ##这个函数是处理套图地址获得图片的页面地址
        html = self.request(url)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span)+1):
        #for page in range(1, 3):
            print "正在保存：", str(page)
            page_url = url + '/' + str(page)
            self.img(page_url) ##调用img函数

    def img(self, page_url): ##这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)
 
    def save(self, img_url): ##这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def up(self): ##将baidu文件夹下的内容全部上传到百度云，然后删除本地全部内容
        os.chdir('..') ##切换到baidu目录
        print u"正在向百度云上传"
        os.system('bypy upload')
        os.system('bypy rm .AppleDouble')
        os.system('rm -rf *')
        print u"上传结束，已删除baidu文件夹内的数据"

    def mkdir(self, path): ##这个函数创建文件夹
        os.chdir('./baidu') ##切换到baidu目录
        path = path[:10]
        isExists = os.path.exists(path)
        if not isExists:
            print u'在baidu下创建了一个名字叫做', path, u'的文件夹！'
            os.mkdir(path)
            os.chdir(path) ##切换到目录
            return True
        else:
            print u'名字叫做', path, u'的文件夹已经存在了！'
            return False
 
    def request(self, url): ##这个函数获取网页的response 然后返回
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content
 
Mzitu = mzitu() ##实例化

your_url = raw_input("输入想要下载的URL地址：")
Mzitu.get_name(your_url) ##给函数all_url传入参数,可以当作启动爬虫的入口

