"""
修改功能模块
"""

from pymysql import *
import menu
info_list = []

# 创建connection连接
conn = connect(host="localhost", user="root", password="root", db="pms", port=3306)


def member_change():
    """人员调配管理"""
    print('-'*50)
    print('功能：查找需要调配的员工')
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
    print('-'*50)
    global num  # 在函数内用global定义变量，变量外就可使用该变量
    num = input("请输入需要修改员工的ID:")
    menu.change()
    action = input('请选择操作功能：')
    print('你选择的功能序号是：{}'.format(action))
    if action in ['1', '2', '3', '4', '5', '0']:
        if action == '1':
            change_name()
        elif action == '2':
            change_work()
        elif action == '3':
            change_site()
        elif action == '4':
            change_time()
        elif action == '5':
            delete_member()
        elif action == '0':
            print("返回")

    else:
        print("你的输入有误")




def change_name():
   """人员姓名修改"""
   print('-' * 50)
   print('功能：姓名修改')
   # 获取cursor对象
   cs1 = conn.cursor()
   name = input("请输入变更后的姓名:")
   # 执行sql语句
   sql1 = "UPDATE member set name='{}' WHERE id={}".format(name,num)
   sql = "SELECT * FROM member WHERE id"
   try:
       cs1.execute(sql1)
       conn.commit()
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
       # 如果发生错误则回滚
       conn.rollback()
       print("更新失败")
   # 关闭光标对象
   cs1.close()
   # 关闭数据库连接
   conn.close()



def change_work():
   """人员工作岗位修改"""
   print('-' * 50)
   print('功能：变更工作岗位')
   # 获取cursor对象
   cs1 = conn.cursor()
   name = input("请输入变更后的工作岗位:")
   # 执行sql语句
   sql1 = "UPDATE member set work='{}' WHERE id={}".format(name,num)
   sql = "SELECT * FROM member WHERE id"
   try:
       cs1.execute(sql1)
       conn.commit()
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
       # 如果发生错误则回滚
       conn.rollback()
       print("更新失败")
   # 关闭光标对象
   cs1.close()
   # 关闭数据库连接
   conn.close()



def change_site():
   """人员工作地点修改"""
   print('-' * 50)
   print('功能：变更工作地点')
   # 获取cursor对象
   cs1 = conn.cursor()
   name = input("请输入变更后的工作地点:")
   # 执行sql语句
   sql1 = "UPDATE member set site='{}' WHERE id={}".format(name,num)
   sql = "SELECT * FROM member WHERE id"
   try:
       cs1.execute(sql1)
       conn.commit()
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
       # 如果发生错误则回滚
       conn.rollback()
       print("更新失败")
   # 关闭光标对象
   cs1.close()
   # 关闭数据库连接
   conn.close()


def change_time():
   """人员工作时间修改"""
   print('-' * 50)
   print('功能：变更工作时间')
   # 获取cursor对象
   cs1 = conn.cursor()
   name = input("请输入变更后的工作时间:")
   # 执行sql语句
   sql1 = "UPDATE member set time='{}' WHERE id={}".format(name,num)
   sql = "SELECT * FROM member WHERE id"
   try:
       cs1.execute(sql1)
       conn.commit()
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
       # 如果发生错误则回滚
       conn.rollback()
       print("更新失败")
   # 关闭光标对象
   cs1.close()
   # 关闭数据库连接
   conn.close()


def delete_member():
   """人员档案删除修改"""
   print('-' * 50)
   print('功能：人员档案删除')
   print('请输入Y/N:')
   decide = input('请最后确认是否删除档案:')
   if decide in ['Y', 'N']:
       if decide == 'Y':
           # 获取cursor对象
           cs1 = conn.cursor()
           # 执行sql语句
           sql1 = "DELETE FROM member WHERE id={}".format(num)
           sql = "SELECT * FROM member WHERE id"
           try:
               cs1.execute(sql1)
               conn.commit()
               cs1.execute(sql)
               result = cs1.fetchall()
               for alist in result:
                   id = alist[0]
                   name = alist[1]
                   work = alist[2]
                   site = alist[3]
                   time = alist[4]
                   print("| ID%d | 姓名:%s | 岗位:%s | 地点:%s | 时间:%s |" % (id, name, work, site, time))
               print('-' * 50)
               print('删除成功')
               print('-' * 50)
           except:
               # 如果发生错误则回滚
               conn.rollback()
               print("更新失败")
           # 关闭光标对象
           cs1.close()
           # 关闭数据库连接
           conn.close()
       elif decide == 'N':
           print("取消删除操作")
   else:
       print('你的输入有误')