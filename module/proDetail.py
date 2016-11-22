# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from module.urlManager import GetPage

from module.savePhoto import DownPhotos
from module.writeFile import WriteFile


class ProDetail(object):
    def __init__(self, bsObj,path):
        self.bsObj = bsObj
        self.path=path
    def getContent(self):
        tempBsObj=GetPage(self.bsObj.attrs['data-tfs-url']).getDetail()
        return BeautifulSoup(tempBsObj,'lxml',from_encoding='GBK')
    def getContentTxt(self):
        contentTxt=self.getContent().get_text()
        WriteFile(self.path,'介绍文字.txt',contentTxt).write()
    def getContentPhotos(self):
        proDetailImgs=list()
        for proImg in self.getContent().findAll('img'):
            tempSrc=proImg.attrs['src'].replace('\\"', '')
            if 'http:' not in tempSrc and 'https:' not in tempSrc:
                tempSrc='http:'+tempSrc
            proDetailImgs.append(tempSrc)
        return proDetailImgs
    def saveContentPhotos(self):
        DownPhotos(self.getContentPhotos(),self.path+'/详情图').save()





