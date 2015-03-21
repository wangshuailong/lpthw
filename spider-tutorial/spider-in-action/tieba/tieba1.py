# !/usr/bin/dev python
# -*- coding: utf-8 -*-

__author__ = 'Wang Shuailong'

import urllib
import urllib2
import re

# http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

class TB(object):

    def __init__(self, baseurl, sl):
        self.baseUrl = baseurl
        self.agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0)'
        self.header = {'User-Agent': self.agent}
        self.sl = '?see_lz='+str(sl)
        
    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.sl + '&pn=' + str(pageNum)
            request = urllib2.Request(url, headers = self.header)
            response = urllib2.urlopen(request)
            pageDoc = response.read()
#            print response.read()
            return pageDoc
        except urllib2.URLError, e:
            if hasattr(e, code):
                print 'e.code: ', e.code
            if hasattr(e, reason):
                print 'e.reason: ', e.reason
    def getTitle(self):
        pageContent = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, pageContent)
        if result:
            print result.group(1).strip()
        else:
            return None
                
baseurl = 'http://tieba.baidu.com/p/3138733512'
tb = TB(baseurl, 1)
tb.getTitle()
        
    

        
