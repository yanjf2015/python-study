#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2, cookielib


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

    def downloadByParam(self, url, *params):
        if url is None or params is None:
            return None
        request = urllib2.Request(url)
        for param in params:
            request.add_data(param.key, param.value)
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()

    def downloadAuth(self, url):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.build_opener(opener)
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()