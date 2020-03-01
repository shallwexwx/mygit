# coding=utf-8
import json
import os

from mysqltools import MySQL


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

    @staticmethod
    def write(file_name1):
        try:
            with open(file_name1)as f:
                res2 = '{' + f.read().split('{', 1)[1]
                res2 = json.loads(res2)
                key_list1 = []
                for key1, value1 in res2.items():
                    print(key1, ':', value1)
                    pass
        except Exception as e2:
            print(e2)
        finally:
            pass


if __name__ == '__main__':
    file_path = str(os.path.abspath(__file__).rsplit('/', 1)[0]) + '/lgo/'
    print(file_path)
    # file_path = '/Users/axin/Desktop/git_work/mygit/work/lgo/' + 'test.log'
    # file_name = '/Users/axin/Desktop/git_work/mygit/work/lgo/test.log'  # mac
    # res = (file_path == file_name)
    # file_path = r'C:\Users\admin\Desktop\work\mygit\work\lgo'  # windows
    mon1 = Monitoring(file_path)
    # print(mon1)

    while 1:
        try:
            # file_name = '/Users/axin/Desktop/git_work/mygit/work/lgo/test.log'
            files = os.listdir(mon1.path)
            for file_name in files:
                # f_name = str(mon1.path + file_name).replace(' ', '')
                f_name = mon1.path + file_name
                print(type(f_name))
                with open(f_name, 'r') as f1:
                    res4 = '{' + f1.read().split('{', 1)[1]
                    res4 = json.loads(res4)
                    # print(type(res))  # <class 'dict'>
                    # key_dir = {}
                    # for key, value in res4.items():
                    #     key_dir[key] = value
                    sql1 = MySQL()
                    conn1 = sql1.create_con()
                    insert_data = sql1.add_data(res4)
            # print(f_name)
            break
        except Exception as e1:
            print(e1)
        # sleep(5)
