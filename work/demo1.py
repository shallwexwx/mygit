# coding=utf-8
import json
import os


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

    @staticmethod
    def find_dir():
        try:
            res = os.getcwd()
            print(res)
        except Exception as e:
            print(e)

    def write(self):
        try:
            with open(self.path)as f:
                res = '{' + f.read().split('{', 1)[1]
                res = json.loads(res)
                key_list = []
                for key, value in res.items():
                    print(key, ':', value)
                    pass
        except Exception as e1:
            print(e1)
        finally:
            pass


if __name__ == '__main__':
    file_path = [os.path.abspath(__file__)]
    m = Monitoring(file_path)
    print(m)
    m.find_dir()
    while 1:
        path = m.path
        files = os.listdir(path)
        for file_name in files:
            f = str(path+file_name)
