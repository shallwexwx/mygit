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
            # 想用嵌套字典判断层数，然后自动生成表，失败
            transaction_time = data["transaction"]["time"]
            transaction_data = data["transaction"]["transaction_id"]
            remote_address = data["transaction"]["remote_address"]
            remote_port = data["transaction"]["remote_port"]
            local_address = data["transaction"]["local_address"]
            local_port = data["transaction"]["local_port"]
            audit_data = data["audit_data"]

            request_line = data["request"]["request_line"]
            request_headers_host = data["request"]["headers"]["Host"]
            request_headers_agent = data["request"]["headers"]["User-Agent"]
            request_headers_accept = data["request"]["headers"]["Host"]
            request_headers_cont_len = data["request"]["headers"]["Content-Length"]
            request_headers_cont_type = data["request"]["headers"]["Content-Type"]
            request_body = data["request"]["body"]

            response_protocol = data["response"]["protocol"]
            response_status = data["response"]["status"]
            response_headers_last_modified = data["response"]["headers"]["Last-Modified"]
            response_headers_tag = data["response"]["headers"]["ETag"]
            response_headers_accept_ranges = data["response"]["headers"]["Accept-Ranges"]
            response_headers_cont_len = data["response"]["headers"]["Content-Length"]
            response_headers_cont_type = data["response"]["headers"]["Content-Type"]
            response_body = data["response"]["body"]

            my_cursor = self.conn.cursor()
            my_cursor.execute('use log_res;')
            insert_data = """
                insert into transaction
                (time, remote_address, remote_port, local_address, local_port, audit_data, transaction_data)
                values ("%s", "%s", "%s", "%s", "%s", "%s", "%s");
            """ % (transaction_time, remote_address, remote_port, local_address,
                   local_port, audit_data, transaction_data)

            select_id = """
                select transaction_id 
                from transaction
                where transaction_data=%s
            """ % (transaction_data,)

            print(insert_data)
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

