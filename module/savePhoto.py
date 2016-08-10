# -*- coding:utf-8 -*-
import os

from urllib import request


class DownPhotos(object):
    def __init__(self, urls, path):
        self.urls = urls
        self.path = path
    def createStorePath(self,url):
        return './'+self.path+'/'+url.split('/')[-1]
    def save(self):
        for imgUrl in self.urls:
            filePath=self.createStorePath(imgUrl)
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            if not os.path.exists(filePath):
                request.urlretrieve(imgUrl, filePath)
            else:
                print('图片已经存在')
