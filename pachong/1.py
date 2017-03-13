#-*- coding:utf-8 -*-
__author__ = 'tony'

# import urllib2
# # response = urllib2.urlopen("http://www.baidu.com")
# # print response
# request = urllib2.Request('http://www.baidu.com')
# response = urllib2.urlopen(request)
# print response.read()

#模拟CSDN登陆 POST方法

# import urllib
# import urllib2
#
# values = {'username':'154293106@qq.com','password':"19840807hxc!"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()

# #模拟CSDN登陆 GET方法
# import urllib
# import urllib2
# values = {}
# values['username']='154293106@qq.com'
# values['password']='19840807hxc!'
# data = urllib.urlencode(values)
# url = 'http://passport.csdn.net/account/login'
# geturl = url+'?'+data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print geturl
# print response.read()

#知乎登陆测试
# import urllib
# import urllib2
#
# url = 'https://www.zhihu.com/'
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# values = {'username':'154293106@qq.com','password':'19840807hxc!'}
# headers = {'User-Agent':user_agent}
# data = urllib.urlencode(values)
# request = urllib2.Request(url,data,headers)
# response = urllib2.urlopen(request)
# page = response.read()

import urllib2
import re
import threading
import time

class Tool:
    def pTitle(self):
        #定义标题抓取的规则
        return re.compile('<title.*?>(.*?)</', re.S)
    def pContent(self):
        #定义内容抓取的规则
        return re.compile(
            '<div class="author.*?>.*?<a.*?<img.*?/>(.*?)</a>.*?</div>.*?<div.*?class="content.*?>(.*?)</div>.*?class="number.*?>(.*?)</.*?',
            re.S)

class QSBK(threading.Thread):
    def __init__(self,max_page):
        threading.Thread.__init__(self,name='tony_thread')
        self.baseUrl = 'http://www.qiushibaike.com/hot/page/'
        self.maxPage = int(max_page) + 1
        self.tool = Tool()

    def getPageContent(self,pageNum):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        url = self.baseUrl + str(pageNum)
        try:
            request = urllib2.Request(url,headers=headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8','ignore')
            content = content.encode('gbk','ignore')
            return content
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u'error:',e.reason
                return None


    def getPageDetail(self,c):
        items = re.findall(self.tool.pContent(),c)
        result = []
        for item in items:
            p = {}
            p['发布人'] = item[0].strip()
            p['id'] = item[2].strip()
            p['内容'] = item[1].strip()
            result.append(p)
        return result

    def getTitle(self,c):
        result = re.findall(self.tool.pTitle(),c)
        return result[0].strip()

    def run(self):
        print '---' + time.ctime() +'---\n'
        for page in range(1,self.maxPage):
            c = self.getPageContent(page)
            if c == None:
                print('URL已经失效，请重试')
                return

            print '---正在抓取第'+str(page)+'页 ---'
            title = self.getTitle(c)
            f = open(title + ' - Page_'+str(page) +'.txt','w')
            result = self.getPageDetail(c)
            cutLine = u'-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.'
            for item in result:
                f.write(cutLine)
                for K,V in item.items():
                    f.write(str(K)+' : '+str(V)+'\n')
            print '---第'+str(page)+'页抓取完毕 ---\n'

            f.close()
            del result
            del f
            del cutLine
            del c
        print '---'+time.ctime()+'---'

maxPage = raw_input('请输入想抓取的最大页数：')
qsbk = QSBK(maxPage)
qsbk.start()
























