# -*- coding: utf-8 -*-
from urllib import request


class GetPage(object):
    def __init__(self, url):
        self.url = url

    def getDetail(self):
        req = request.Request(self.url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36')
        with request.urlopen(self.url) as html:
            data = html.read()
            print('status', html.status, html.reason)
        return data
