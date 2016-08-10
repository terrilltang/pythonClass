# -*- coding:utf-8 -*-

from module.savePhoto import DownPhotos

class GetMainImages(object):
    def __init__(self, bsObj, filePath):
        self.bsObj = bsObj
        self.filePath = filePath

    def getImages(self):
        images = list()
        mainPhoto = self.bsObj.findAll('li', class_='tab-trigger')

        for tag in mainPhoto:
            originalImg = eval(tag.attrs['data-imgs'])['original']
            if originalImg:
                images.append(originalImg)
        return images

    def downImages(self):
        photos = self.getImages()
        DownPhotos(photos, self.filePath).save()
