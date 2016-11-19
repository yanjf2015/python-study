#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2, cookielib


class HtmlDownloader(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}
    @staticmethod
    def download(self,url):
        if url is None:
            return None
        req = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(req)
        if response.getcode() != 200:
            return None
        return response.read()

    @staticmethod
    def download_by_param(self, url, *params):
        if url is None or params is None:
            return None
        request = urllib2.Request(url)
        for param in params:
            request.add_data(param.key, param.value)
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()

    @staticmethod
    def download_auth(self, url):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.build_opener(opener)
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()