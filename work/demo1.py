# coding=utf-8
import os
import sys

import pymysql


class Monitoring:
    def __init__(self, path_list):
        self.path_list = path_list  # 传入一个文件夹路径

    # def __str__(self):
    #     return self.path_list

    def exist_create_dir(self):
        for item in self.path_list:
            try:
                res = os.path.exists(item)
            except Exception as e:
                os.makedirs(item)
                res = True
                print(e)
            return res

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
