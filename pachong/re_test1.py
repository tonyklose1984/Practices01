#-*- coding:utf-8 -*-
__author__ = 'tony'
import re

# pattern = re.compile(r' CQC!')
#
# result1 = re.match(pattern,'hello')
# result2 = re.match(pattern,'hello CQC!')
# result3 = re.match(pattern,'helo CQC!')
# result4 = re.match(pattern,'hello CQC!')
#
# if result1:
#     print result1.group()
# else:
#     print '1匹配失败'
#
# if result2:
#     print result2.group()
# else:
#     print "2匹配失败"
#
# if result3:
#     print result3.group()
# else:
#     print "3匹配失败"
#
# if result4:
#     print result4.group()
# else:
#     print "4匹配失败"

# m = re.match(r'(\w+)(\w+)(?P<sign>.*)','hello world!')
# print 'm.string:',m.string
# print 'm.re:',m.re
# print 'm.pos:',m.pos
# print 'm.endpos:',m.endpos
# print 'm.lastindex:',m.lastindex
# print 'm.lastgroup:',m.lastgroup
# print "m.group:",m.group()
# print "m.group(1,2),m.group(1,2)"
# print "m.groups():",m.groups()
# print "m.groupdict():",m.groupdict()
# print "m.start(2):",m.start(2)
# print "m.end(2):",m.end(2)
# print "m.span(2):",m.span(2)
# print r"m.expand(r'\g \g\g'):",m.expand(r'\2 \1\3')

import re
word = "abidsabifdasbifdsbigbi"
nojoke=re.findall(r'bi',word)
print nojoke
nojoke=re.findall(r"^abi",word)
print nojoke
nojoke=re.findall(r"abi",word)
print nojoke
nojoke=re.findall(r"gbi$",word)
print nojoke
nojoke=re.findall(r"[abc]f","afufobfufocfufo")
print nojoke
word2="abi11dsabi2fdasbi3fdsbi4gbi55"
nojoke=re.findall(r"\d",word2)
print nojoke
nojoke=re.findall(r"\D",word2)
print nojoke
word3="abi11bi2f3fdsbi4gb555666"
nojoke=re.findall(r"\d\d\d",word3)
print nojoke
word4="a11b2@@@f3fDs###4GI***"
nojoke=re.findall(r"\w",word4)
print nojoke
nojoke=re.findall(r"\W",word4)
print nojoke
nojoke = re.findall(r"<div>(.*?)</div>","<div>hello1</div><div>hello2</div>")
print nojoke
nojoke = re.findall(r"<div>*?</div>","<div>hello1</div><div>hello2</div>")
print nojoke
nojoke = re.findall(r"<div>(.*)</div>","<div>hello1</div><div>hello2</div>")
print nojoke
nojoke = re.findall(r"<div>(.*?)</div>","<div>hello1</div><div>hello2</div>")
print nojoke
nojoke = re.findall(r"<div>(hello)</div>","<div>hello</div>")
print nojoke
nojoke = re.findall(r"<div>(.*)</div>","<div>heLLo\nw*\[]ord</div>",re.I)
print nojoke
nojoke = re.findall(r"<div>(.*)</div>","<div>heLLo\nw*\[]ord</div>",re.I|re.S)
print nojoke
#match和search的用法及区别
print(re.match('www','www.runoob.com').span())
print(re.match('com','www.runoob.com'))
print(type(re.search('www','www.runoob.com').span()))
print(re.search('com','www.runoob.com').span())






















