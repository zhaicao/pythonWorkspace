from pymysql import cursors, connect

# 连接数据库
conn = connect(host='127.0.0.1',
               user='root',
               password='root',
               db='guest',
               charset='utf8',
               cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'insert into guest(realname,phone,email,sign,event_id,create_time) values ("tom",18800110002,"tom@mail.com",0,1,NOW()); '
        cursor.execute(sql)
    # 提交事务
    conn.commit()
    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = "select * from guest where phone=%s"
        cursor.execute(sql, ('18800110002',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()