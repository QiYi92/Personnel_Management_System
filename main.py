import tools

while True:

    tools.show_menu()

    action = input('请选择操作功能：')
    print('你选择的功能序号是：{}'.format(action))
    if action in ['1', '2', '3', '4', '5']:
        if action == '1':

            tools.opt_menu()

            opt = input('请选择新建人员类型:')
            if opt in ['1','2']:
                if opt == '1':
                    tools.new_employee1()
                elif opt == '2':
                    tools.new_employee2()
            else:
                print('你的输入有误')

        elif action == '2':  # 部门信息维护
            tools.search_divison()

        elif action == '3':  # 人员信息维护
            tools.show_all()

        elif action == '4':  # 人员调配管理
            tools.search_change()

        elif action == '5': # 人员分布查询
            tools.search_member()

    elif action == '0':
        print('欢迎再次使用')
        break

    else:
        print('你的输入有误')
