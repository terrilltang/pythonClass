# -*- coding:utf-8 -*-
import os
class WriteFile(object):
    def __init__(self, path, file,str):
        self.path = path
        self.file=file
        self.str = str

    def write(self):
        print(os.path.join(self.path,self.file))
        with open(os.path.join(self.path,self.file), 'w',encoding='utf-8') as f:
            f.write(str(self.str))
        print('文件写入成功')
