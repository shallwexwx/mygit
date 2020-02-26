import os

import json
import pymysql

host = 'Localhost'
user = 'root'
pwd = 'xwx961103'
port = 3306
charset = 'utf8'
db = 'res1'


def connect_mysql():
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            port=port,
            charset=charset,
            # db=db
        )
    except Exception as e:
        print(e)
        conn = False

    my_cursor = conn.cursor()
    my_cursor.execute('CREATE DATABASE log_res')
    return conn


if __name__ == '__main__':
    # res = os.getcwd()
    # print(res)
    with open(r'E:/lgo/test.log')as f:
        res = '{' + f.read().split('{', 1)[1]
        res = json.loads(res)
        # print(type(res))  # <class 'dict'>
        key_list = []
        for key, value in res.items():
            print(key, ':', value)
            pass
