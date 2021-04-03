info_list = []

def show_menu():
    """显示菜单"""
    print('-' * 50)
    print("""
'  ########     ##     ##     ######  
'  ##     ##    ###   ###    ##    ## 
'  ##     ##    #### ####    ##       
'  ########     ## ### ##     ######  
'  ##           ##     ##          ## 
'  ##           ##     ##    ##    ## 
'  ##           ##     ##     ######  
    """)
    print('-' * 50)
    print('Personnel Management System --V2.2')
    print('欢迎使用单位人员管理系统V2.2')
    print('开发者——软件工程1班 黄祺熠')
    print('')
    print('[1] 新建人员档案')
    print('[2] 部门信息维护')
    print('[3] 人员信息维护')
    print('[4] 人员调配管理')
    print('[5] 人员分布查询')
    print('')
    print('[0] 退出系统')
    print('-' * 50)

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

    # 提示用户输入员工信息
    name = input('请输入员工姓名:')
    work = '※机关'
    site = '※机关'
    time = '※长期'

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

    # 提示用户输入员工信息
    name = input('请输入员工姓名:')
    work = input('请输入员工岗位:')
    site = input('请输入员工工作地点:')
    time = input('请输入员工工作时间(格式：xx-xx 例子：04-27):')

    # 保存到字典
    info_dict = {
        'name': name,
        'work': work,
        'site': site,
        'time': time,
    }

    info_list.append(info_dict)

    print(">>>成功添加第二类员工{}<<<".format(info_dict["name"]))


def search_divison():
    """部门信息维护"""
    print('-'*50)
    print('功能：对应部门的员工分布')

    # 根据要搜索的姓名
    find_work = input('请输入要搜索的部门:')

    # 遍历
    for employee_dict in info_list:
        if employee_dict['work'] == find_work:

            print("姓名\t\t\t岗位\t\t\t地点\t\t\t时间")
            print('-'*50)

            print('{}\t\t\t{}\t\t\t{}\t\t\t{}'.format(employee_dict['name'],
                                                      employee_dict['work'],
                                                      employee_dict['site'],
                                                      employee_dict['time'],))
            print('-'*50)
            break
        else:
            print("无{}部门或该部门无人员分布".format(find_work))


def show_all():
    """人员信息维护-显示全部"""
    print('-' * 50)
    print('功能：显示全部')
    print('注:带有※则表示此项不可更改')
    print('-' * 50)


    if len(info_list) == 0:
        print('提示：没有任何名片记录')


        return

    for name in ['姓名', '岗位', '地点', '时间']:
        print(name, end='\t\t')

    print('')
    print('='*50)
    for employee_info in info_list:
        print('{}\t\t{}\t\t{}\t\t{}' .format(employee_info['name'],
                                             employee_info['work'],
                                             employee_info['site'],
                                             employee_info['time'])),

def search_change():
    """人员调配管理"""
    print('-'*50)
    print('功能：查找需要调配的员工')

    # 根据要搜索的时间
    find_name = input('请输入要搜索的员工:')

    # 遍历
    for employee_dict in info_list:
        if employee_dict['name'] == find_name:

            print("姓名\t\t\t岗位\t\t\t地点\t\t\t时间")
            print('-'*50)

            print('{}\t\t\t{}\t\t\t{}\t\t\t{}'.format(employee_dict['name'],
                                                      employee_dict['work'],
                                                      employee_dict['site'],
                                                      employee_dict['time'],))
            print('-'*50)
            deal_employee(employee_dict)
            break
        else:
            print("时间{}内无人员分布".format(find_name))


def search_member():
    """人员分布查询"""
    print('-'*50)
    print('功能：查找当天员工分布')

    # 根据要搜索的时间
    find_time = input('请输入要搜索的时间(格式：xx-xx 例子：04-27):')

    # 遍历
    for employee_dict in info_list:
        if employee_dict['time'] == find_time:

            print("姓名\t\t\t岗位\t\t\t地点\t\t\t时间")
            print('-'*50)

            print('{}\t\t\t{}\t\t\t{}\t\t\t{}'.format(employee_dict['name'],
                                                      employee_dict['work'],
                                                      employee_dict['site'],
                                                      employee_dict['time'],))
            print('-'*50)
            deal_employee(employee_dict)
            break
        else:
            print("时间{}内无人员分布".format(find_time))




def deal_employee(find_dict):
    """人员的调配管理"""
    print(find_dict['time'],"时间内所有员工搜索完毕")

    action_str = input('[1]修改\n[2]删除\n[0]返回主菜单\n'
                       '请选择要操作的序号:')

    if action_str == '1':
        print('-' * 50)
        print("修改人员信息")
        print('-' * 50)


        find_dict['name'] = input_employee_info(find_dict['name'], "输入调配员工的姓名:")
        find_dict['work'] = input_employee_info(find_dict['work'], "输入新的工作岗位:")
        find_dict['site'] = input_employee_info(find_dict['site'], "输入新的工作地点:")
        find_dict['time'] = input_employee_info(find_dict['time'], "输入新的工作时间:")

        print(">>>{}的档案修改成功<<<".format(find_dict["name"]))

    elif action_str == '2':
        print("删除中...")
        info_list.remove(find_dict)
        print(">>>删除成功<<<")

def input_employee_info(dict_value, tip_message):
    """输入名片信息"""
    ret_str = input(tip_message)

    # 针对用户输入的内容进行判断。如果有值，则直接返回结果
    if len(ret_str) > 0:
        return ret_str
    else:
        return dict_value