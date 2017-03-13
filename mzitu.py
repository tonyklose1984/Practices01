#-*- coding:utf-8 -*-
__author__ = 'tony'
import urllib
import random
import time
from datetime import datetime,timedelta
import socket

DEFAULT_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 60

class Downloader:
    def __init__(self,user_agent=DEFAULT_AGENT,proxies=None,num_retries=DEFAULT_RETRIES,timeout=DEFAULT_TIMEOUT,opener=None, cache=None):
        socket.setdefaulttimeout(timeout)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache

    def __call__(self,url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries > 0 and 500 <= result['code'] < 600:
                    result = None
        if result is None:
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-Agent':self.user_agent}
            result = self.download(url,headers,proxy=proxy,num_retries=self.num_retries)
            if self.cache:
                self.cache[url] = result
            return result['html']

    def download(self,url,user_agent=DEFAULT_AGENT,proxy=None,num_retries=2):
        print('Downloading:',url)
        headers = {'User-Agent':user_agent}
        request = urllib.request.Request(url, headers=headers)
        opener = urllib.request.build_opener()
        if proxy:
            # proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
            opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy))
        try:
            # html = urllib.request.urlopen(request).read().decode('utf-8')
            urllib.request.install_opener(opener)
            html = urllib.request.urlopen(url).read().decode('utf-8')
        except urllib.error.URLError as e:
            print('Download error:', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # retry 5XX HTTP errors
                    return self.download(url, user_agent, proxy, num_retries - 1)

        return html
