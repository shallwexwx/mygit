import pymysql


class MySQL:
    def __init__(self, host='106.15.39.103', user='root',
                 pwd='xwx961103', db=0, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port
        self.charset = charset
        self.conn = None

    def create_con(self):
        self.conn = False
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.pwd,
                port=self.port,
                charset=self.charset,
                # db=self.db
            )
        except Exception as e:
            print(e)
        finally:
            return self.conn

    def create_database(self):
        cre_res = ''
        try:
            my_cursor = self.conn.cursor()
            cre_res = my_cursor.execute('create database if not exists log_res '
                                        'character set utf8mb4 '
                                        'collate utf8mb4_general_ci')
        except Exception as e1:
            print(e1)
        finally:
            return cre_res

    def create_table(self):
        already = True
        # if column_names is None:
        #     column_names = ["transaction", "request", "response", "audit_data"]
        try:
            my_cursor = self.conn.cursor()
            my_cursor.execute('use log_res;')
            # my_cursor.execute('drop table if exists data;')
            create_table_sql = """
                create table data(
                    id int not null,
                    transaction text default null,
                    request text default null,
                    response text default null,
                    audit_data text default null
                )engine=innodb DEFAULT CHARACTER set utf8mb4;
            """
            re = my_cursor.execute(create_table_sql)
            print(re)
        except pymysql.Error as e:
            print(e)
            already = False
        return already

    def add_data(self, data):
        already = True
        try:
            my_cursor = self.conn.cursor()
            insert_data = """
                insert into data
                ("transaction", "request", "response", "audit_data")
                values
                (%s, %s, %s, %s)
            """ % (data["transaction"], data["request"],
                   data["response"], data["audit_data"])
            my_cursor.execute(insert_data)
        except Exception as e3:
            print(e3)
            already = False
        return already


if __name__ == '__main__':
    con1 = MySQL()
    res = con1.create_con()
    # res1 = con1.create_database()
    res2 = con1.create_table()
    print(res)

