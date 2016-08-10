# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

from module.proDetail import ProDetail
from module.proParams import ProductParam
from module.urlManager import GetPage
from module.mainPhotos import GetMainImages

# url = 'https://detail.1688.com/offer/521394873283.html?spm=0.0.0.0.aVtADK'
# url = 'https://detail.1688.com/offer/530258840255.html?spm=0.0.0.0.aVtADK'
# url = 'https://detail.1688.com/offer/530258840255.html?spm=0.0.0.0.H5ZTp0'
url = 'https://detail.1688.com/offer/535774264882.html?spm=0.0.0.0.H5ZTp0'

resource = open('./URLS.txt', 'r').readlines()



def getProDetail(url):
    bsObj = BeautifulSoup(GetPage(url).getDetail(), 'lxml')

    # 获取标题
    proTitle = bsObj.find('h1', class_='d-title').get_text()

    # 获取主图
    GetMainImages(bsObj, '商品/' + proTitle + '/缩略图').downImages()

    # 获取参数
    ProductParam(bsObj, '商品/' + proTitle, '参数.json').saveParams()

    # 获取详情内容及图片

    proDetailObj = bsObj.find('div', class_='desc-lazyload-container')

    ProDetail(proDetailObj, '商品/' + proTitle).getContentTxt()
    ProDetail(proDetailObj, '商品/' + proTitle).saveContentPhotos()


for url in resource:
    getProDetail(url.replace('\r\n', ''))