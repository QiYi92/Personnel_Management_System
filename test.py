from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host="localhost", user="root", password="root", db="pms", port=3306)
    # 获取cursor对象
    cs1 = conn.cursor()
    # 执行sql语句
    query = 'insert into member(name,work,site,time) values(%s,%s,%s,%s)'
    name = input('请输入员工姓名:')
    work = '※机关'
    site = '※机关'
    time = '※长期'
    values = (name, work, site, time)
    cs1.execute(query, values)

    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    conn.commit()

    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()


if __name__ == '__main__':
    main()