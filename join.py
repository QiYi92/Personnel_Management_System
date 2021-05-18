"""
新建功能模块
"""
from pymysql import *
info_list = []

# 创建connection连接
conn = connect(host="localhost", user="root", password="root", db="pms", port=3306)


def opt_menu():
    """人员类型选择菜单"""
    print('-' * 50)
    print('请选择新建人员的档案类型:')
    print('')
    print('[1] 新建机关人员档案')
    print('[2] 新建流动人员档案')

def new_employee1():
    """新建第一类机关人员"""
    print('-' * 50)
    print('功能：新增机关员工')
    print('>>>不可更改岗位和地点<<<')

    # 数据库
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

    # 保存到字典
    info_dict = {
        'name': name,
        'work': work,
        'site': site,
        'time': time,
    }

    info_list.append(info_dict)

    print("成功添加第一类员工:{}".format(info_dict["name"]))



def new_employee2():
    """新建第二类员工"""
    print('-' * 50)
    print('功能：新增第二类员工')

    # 数据库
    # 获取cursor对象
    cs1 = conn.cursor()
    # 执行sql语句
    query = 'insert into member(name,work,site,time) values(%s,%s,%s,%s)'
    # 提示用户输入员工信息
    name = input('请输入员工姓名:')
    work = input('请输入员工岗位:')
    site = input('请输入员工工作地点:')
    time = input('请输入员工工作时间(格式：xx-xx 例子：04-27):')
    values = (name, work, site, time)
    cs1.execute(query, values)
    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    conn.commit()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()

    # 保存到字典
    info_dict = {
        'name': name,
        'work': work,
        'site': site,
        'time': time,
    }

    info_list.append(info_dict)

    print(">>>成功添加第二类员工{}<<<".format(info_dict["name"]))