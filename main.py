# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

from module.proDetail import ProDetail
from module.proParams import ProductParam
from module.urlManager import GetPage
from module.mainPhotos import GetMainImages



resource = open('./URLS.txt', 'r').readlines()

print(resource)



def getProDetail(url):
    bsObj = BeautifulSoup(GetPage(url).getDetail(), 'lxml')

    # 获取标题
    proTitle = bsObj.find('h1', class_='d-title').get_text().replace('*','').replace('$','').replace('_','').replace('x','')

    # 获取主图
    GetMainImages(bsObj, '商品/' + proTitle + '/缩略图').downImages()

    # 获取参数
    #ProductParam(bsObj, '商品/' + proTitle, '参数.json').saveParams()

    # 获取详情内容及图片

    proDetailObj = bsObj.find('div', class_='desc-lazyload-container')

    #ProDetail(proDetailObj, '商品/' + proTitle).getContentTxt()
    ProDetail(proDetailObj, '商品/' + proTitle).saveContentPhotos()


for url in resource:
    print(url.replace('\n',''))
    getProDetail(url.replace('\n', ''))
