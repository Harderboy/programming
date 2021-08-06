# coding=utf-8
# **第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

import pymysql
from generate_code_001 import generate_code_to_txt


def store_mysql(file_path):
    db = pymysql.connect(host="127.0.0.1", user="root",
                         passwd="123456", database="ShowMeTheCode")
    cursor = db.cursor()

    # 检查表是否存在，存在则删除
    cursor.execute("drop table if exists coupon_code")

    # 建表
    sql = "create table coupon_code(id int auto_increment primary key, code varchar(50) not null)"
    # 使用 execute() 方法执行 SQL 语句
    cursor.execute(sql)

    with open(file_path, 'r') as f:
        result = f.readlines()
        # print(result)
    for line in result:
        code = line.strip()
        # print(code)

        # 注意规范写法，在数据库表和字段上加反引号
        sql = "insert into `coupon_code` (`code`) values (%s)"
        # print(sql)

        # cursor.execute(sql,param)，param应该为tuple或者list或者字典（比较特殊）%(name)s
        """
        d = {'age':'5'}
        sql = 'select * from student where age>%(age)s'
        print(sql)
        line = cursor.execute(sql,d)
        """
        try:
            cursor.execute(sql, (code,))
            # 事务
            db.commit()
        except:
            # 提交失败，回滚到上次操作
            db.rollback()

    # 此处转义与否没有区别 “\*”
    cursor.execute(
        "select * from coupon_code")
    all_data = cursor.fetchall()
    print(all_data)
    # 关闭数据库连接

    cursor.close()
    db.close()

# 读取文件，删除换行字符“\n”
# 打开文件
# fo = open("coupon.txt", "r")
# print ("文件名为: ", fo.name)

# for line in fo.readlines():                          #依次读取每行
#     line = line.strip()                             #去掉每行头尾空白
#     print ("读取的数据为: %s" % (line))

# 关闭文件
# fo.close()


if __name__ == "__main__":
    store_mysql("编程练习/python练习/show-me-the-code/coupon.txt")


'''
学习以下写法，类比文件对象的操作

with connection:
    with connection.cursor() as cursor:

    with connection.cursor() as cursor:


with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
'''
