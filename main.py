#!/usr/bin/python
# -*- coding: UTF-8 -*-
import menu  # 菜单模块
import join  # 新建模块
import search  # 搜索模块
import change  # 删改模块
import pymysql  # 数据库模块
import progress  # 进度条模块

pymysql.install_as_MySQLdb()  # 手动指定将MySqldb转给pymysql处理

# 进度条
progress.progress_bar()


while True:
    try:
        menu.show_menu()

        action = input('请选择操作功能：')
        print('你选择的功能序号是：{}'.format(action))
        if action in ['1', '2', '3', '4', '5']:
            if action == '1':
                join.opt_menu()
                opt = input('请选择新建人员类型:')
                if opt in ['1','2']:
                    if opt == '1':
                        join.new_employee1()
                    elif opt == '2':
                        join.new_employee2()
                    menu.exit()
                else:
                    print('你的输入有误')
                    menu.exit()

            elif action == '2':  # 部门信息维护
                search.search_divison()
                menu.exit()

            elif action == '3':  # 人员信息维护
                search.show_all()
                menu.exit()

            elif action == '4':  # 人员调配管理
                change.member_change()
                menu.exit()

            elif action == '5': # 人员分布查询
                search.search_member()
                menu.exit()
        elif action == '0':
            print('欢迎再次使用')
            break

        else:
            print('你的输入有误')
    except:
        # 如果出现异常则输出此
        print('-' * 50)
        print("ERROR: 数据库异常")
        print('-' * 50)
        menu.exit()