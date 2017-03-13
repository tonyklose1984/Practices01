#-*- coding:utf-8 -*-
__author__ = 'tony'
# import urllib2
# import cookielib
#
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value

#保存Cookie到文件

import urllib2
import cookielib

# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)
#创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# #从文件读取cookie内容到变量
# cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# #创建请求的request
# req = urllib2.Request('http://www.baidu.com')
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

#利用cookie模拟网站登录
# import urllib2
# import cookielib
# import urllib
#
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#     'student':'201200131012',
#     'pwd':'23342321'
# })
# #登录教务处系统的URL
# loginUrl = "http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login"
# #模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# cookie.save(ignore_discard=True,ignore_expires=True)
# #利用cookie请求另一个网址，此网址是成绩查询网址
# gradeUrl = "http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre"
# result = opener.open(gradeUrl)
# print result.read()






















