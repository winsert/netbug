#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 实现从./temp.txt文件中读取下载URL，批量下载完成后，发送微信通知

__author__ = 'winsert@163.com'

from bs4 import BeautifulSoup 
import urllib
import urllib2
import json, os, re
import itchat

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore') 
    bsObj1 = BeautifulSoup(html, "lxml")
    return bsObj1

# 用于记录下载数据
def Schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
        #print '下载进度：%.2f%%' % per
        #print '已下载:',a*b
        print u'文件大小:', round(c/1024/1024.0, 2), 'M'
        #print '已经下载的数据块:',a#,'\n'
        #print '数据块的大小:',b#,'\n'
        #print '远程文件大小:',c,'\n'
        #print '已下载的大小:',a*b,'文件大小:',c

# 用于分析专辑信息，音频文件名称，下载地址，并下载保存在指定文件夹中
def getM4a(url, num):
    bsObj = bsObjForm(url)
    soundInfo=bsObj.p.string
    jsonStr = json.loads(soundInfo)
    album_title=jsonStr['album_title'] #专辑名称
    play_path=jsonStr["play_path"] #音频下载地址
    title=jsonStr["title"] #音频文件的名称

    #由于title里面可能包含不能作文件名称的字符，所以将这些字符去掉
    title= re.sub('[\/:*?"<>|]','_',title)
    print '\n'+"专辑名称：", album_title
    print "音频文件名称：", title
    #print "音频文件的下载URL：", play_path

    #判断文件夹是否存在，如果不存在，则新建文件夹
    if os.path.exists('./download/'+album_title+'/')==False:
        os.makedirs(u'./download/'+album_title+'/')

    # 生成音频文件保存地址
    article_path='./download/'+album_title+'/'+title+'.m4a'

    #判断文件是否存在，如果存在，则不进行下载
    if  os.path.exists(article_path):
        print title, '文件已经存在!!!'
    else:
        print "现在开始下载第%s个音频文件" %num
        urllib.urlretrieve(play_path, article_path, Schedule)
        print "文件已保存到：", article_path
        print

    return album_title

#分析所属专辑内各文件地址 
def getAlbumInfo(url, page):
    bsObj = bsObjForm(url)
    soundIds = bsObj.find('div', attrs={'class':'personal_body'}).get('sound_ids').split(',')
    ids_len = len(soundIds)
    if page == '0': # 如果只有一页
        print "本专辑共有%r个音频文件。" % ids_len
        i = 0
        for i in range(0, 2): #测试只下载2个文件
        #for i in range(0, ids_len):
            soundId = soundIds[i]
            #print "SoundID:", soundId
            path_url='http://www.ximalaya.com/tracks/'+soundId+'.json'
            #print path_url
            msg = getM4a(path_url, str(i+1))  #传递记录有音频下载地址的json页面和下载的序列数
    
        print 
        print "专辑名称：", msg
        print "本专辑共%r个音频文件已全部下载完成。" % ids_len
        print
    else: #如果有多个页面
        print "本页共有%r个音频文件。" % ids_len
        i = 0
        for i in range(0, 2):
        #for i in range(0, ids_len):
            soundId = soundIds[i]
            #print "SoundID:", soundId
            path_url='http://www.ximalaya.com/tracks/'+soundId+'.json'
            #print path_url
            getM4a(path_url, page+'-'+str(i+1)) #传递记录有音频下载地址的json页面和下载的序列数

        print '\n'+'本页共%r个音频文件已全部下载完成。' % ids_len
        print

# 确定专辑的页数。
def getAlbumPages(url):
    pages_resp = bsObjForm(url)
    try:
        temp_list = pages_resp.find('div', class_="pagingBar"    ).find('div', class_="pagingBar_wrapper").find_all('a')
        pages_list = []
        for h in temp_list:
            pages_list.append(h.get_text())
            
        #print pages_list

        pages = len(pages_list)-1 #专辑的页数
        print '\n'+"本专辑共有%d页。" %pages
        for k in range(0, pages):
            page = str(pages_list[k])
            pageUrl = url+"?page="+page
            #print pageUrl
            print '\n'+"现在开始下载第%s页的内容。" %page
            getAlbumInfo(pageUrl, page)
    except: #假如只有一页
        page = '0'
        pageUrl = url
        getAlbumInfo(pageUrl, page) #传递要下载的URL和页码

def getAlbumUrl():
    file = open('./temp.txt', 'r') # 打开存放下载URL地址的temp.txt文件
    file_list = file.readlines()
    file.close()
    num  = len(file_list)
    print "="*30
    print "本次共下载%r个专辑。" % num

    for i in range(num):
        print "\n"+"现在开始下载：", file_list[i]
        url_list = file_list[i].split(',')
        #print url_list[0]
        getAlbumPages (url_list[0])

if __name__ == '__main__':
    
    #itchat.auto_login(hotReload=True)
    getAlbumUrl()
