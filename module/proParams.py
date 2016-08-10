# -*- coding:utf-8 -*-
from module.writeFile import WriteFile


class ProductParam(object):
    def __init__(self, bsObj, path, file):
        self.bsObj = bsObj
        self.path = path
        self.file = file

    def getName(self):
        return self.bsObj.findAll('td', class_='de-feature')

    def getValue(self):
        return self.bsObj.findAll('td', class_='de-value')

    def getParams(self):
        pName = self.getName()
        pValue = self.getValue()
        productParam = list()

        for detail in pName:
            i = pName.index(detail)
            productParam.append({'feature': detail.get_text(), 'value': pValue[i].get_text()})
        return productParam

    def saveParams(self):
        params = self.getParams()
        WriteFile(self.path, self.file, params).write()
