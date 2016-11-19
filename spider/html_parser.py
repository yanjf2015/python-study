#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        # new_data = self._get_new_data(page_url, soup)
        new_data = self._get_html(page_url,html_cont)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r".*manual.*"))
        for link in links:
            new_url = link['href']
            if new_url.startswith('http') or new_url.startswith('mailto'):
                continue
            new_full_url = urlparse.urljoin(page_url, new_url[0:new_url.index('.html')])
            new_urls.add(new_full_url+'.html')
        print 'get new url done'
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_= "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def _get_html(self, page_url, html_cont):
        res_data = {}
        res_data['name'] = page_url[page_url.rindex('/')+1:page_url.index('.html')]+'.html'
        res_data['countent'] = html_cont
        return res_data
