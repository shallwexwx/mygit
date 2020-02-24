# coding=utf-8
import os
import sys

import pymysql


class Monitoring:
    def __init__(self, path):
        self.path = path  # 传入一个文件夹路径

    def __str__(self):
        return self.path

    def exist_create_dir(self):
        try:
            os.path.exists(self.path)
        except Exception as e:
            os.makedirs(self.path)
            print(e)

    def has_new_file(self):
        while 1:
            path = self.path
            pass

    @staticmethod
    def find_dir():
        try:
            res = os.getcwd()
            print(res)
        except Exception as e:
            print('文件夹异常 %s' % e)


if __name__ == '__main__':
    file_path = [os.path.abspath(__file__)]
    m = Monitoring(file_path)
    print(m)
    m.find_dir()
