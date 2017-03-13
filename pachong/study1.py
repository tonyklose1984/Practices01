#-*- coding:utf-8 -*-
__author__ = 'tony'

# import urllib
# import urllib2
# url = "http://www.server.com/login"
# user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
# values = {'username':'cqc','password':'XXXX'}
# headers = {'User-Agent':user_agent}
# data = urllib.urlencode(values)
# request = urllib2.Request(url,data,headers)
# response = urllib2.urlopen(request)
# page = response.read()
#
# #Proxy(代理设置)
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
#
# #3.TimeOut设置
# response = urllib2.urlopen("http://www.baidu.com",timeout=10)
# response = urllib2.urlopen("http://www.baidu.com",data,10)
#
# #4.使用HTTP的PUT和DELETE方法
# request = urllib2.Request(url,data=data)
# request.get_method = lambda: 'PUT'
# response = urllib2.urlopen(request)
#
# #5.使用DebugLog
# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler,httpsHandler)
# urllib2.install_opener(opener)
# response = urllib2.urlopen("http://www.baidu.com")

#1.URLError
# '''
# 首先解释下URLError可能产生的原因：
#
# 网络无连接，即本机无法上网
# 连接不到特定的服务器
# 服务器不存在
# '''
# import urllib2
# request = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError,e:
#     print e.reason

# import urllib2
#
# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError,e:
#     print e.code
# except urllib2.URLError,e:
#     print e.reason
# else:
#     print 'OK'

# import urllib2
# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError,e:
#     if hasattr(e,'reason'):
#         print e.reason
#
# else:
#     print 'OK'

















