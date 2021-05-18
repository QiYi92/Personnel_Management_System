"""
搜索功能模块
"""
from pymysql import *
info_list = []

# 创建connection连接
conn = connect(host="localhost", user="root", password="root", db="pms", port=3306)

def search_divison():
    """部门信息维护"""
    print('-'*50)
    print('功能：对应部门的员工分布')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 根据要搜索的部门
    find_work = input('请输入要搜索的部门:')
    # 触发器
    TF = False
    # 执行sql语句
    # 模糊搜索
    sql = "select * from member where concat(id,name,work,site,time) like '%%{}%%'".format(find_work)
    try:
        cs1.execute(sql)
        result = cs1.fetchall()
        for alist in result:
            id = alist[0]
            name = alist[1]
            work = alist[2]
            site = alist[3]
            time = alist[4]
            print("ID%d | 姓名:%s | 岗位:%s | 地点:%s | 时间:%s"%(id,name,work,site,time))
            TF = True
    except:
        # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
        conn.commit()
        # 关闭cursor对象
        cs1.close()
        # 关闭connection对象
        conn.close()
    if TF == False:
        print('-' * 50)
        print("找不到该岗位或该岗位无人员分布")
        print('-' * 50)


def show_all():
    """人员信息维护-显示全部"""
    print('-' * 50)
    print('功能：显示全部')
    print('注:带有※则表示此项不可更改')
    print('-' * 50)
    # 获取cursor对象
    cs1 = conn.cursor()
    # 执行sql语句
    sql = "SELECT * FROM member WHERE id"
    try:
        cs1.execute(sql)
        result = cs1.fetchall()
        for alist in result:
            id = alist[0]
            name = alist[1]
            work = alist[2]
            site = alist[3]
            time = alist[4]
            print("| ID%d | 姓名:%s | 岗位:%s | 地点:%s | 时间:%s |" % (id, name, work, site, time))
    except:
        # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
        conn.commit()
        # 关闭cursor对象
        cs1.close()
        # 关闭connection对象
        conn.close()
    print('-' * 50)


def search_member():
    """人员分布查询"""
    print('-'*50)
    print('功能：查询对应时间内的员工分布')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 根据要搜索的部门
    find_time = input('请输入要搜索的时间日期:')
    # 触发器
    TF = False
    # 执行sql语句
    # 模糊搜索
    sql = "select * from member where concat(id,name,work,site,time) like '%%{}%%'".format(find_time)
    try:
        cs1.execute(sql)
        result = cs1.fetchall()
        for alist in result:
            id = alist[0]
            name = alist[1]
            work = alist[2]
            site = alist[3]
            time = alist[4]
            print("ID%d | 姓名:%s | 岗位:%s | 地点:%s | 时间:%s"%(id,name,work,site,time))
            TF = True
    except:
        # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
        conn.commit()
        # 关闭cursor对象
        cs1.close()
        # 关闭connection对象
        conn.close()
    if TF == False:
        print('-' * 50)
        print("找不到该岗位或该岗位无人员分布")
        print('-' * 50)