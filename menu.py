"""
菜单功能模块
"""
info_list = []


def show_menu():
    """显示菜单"""
    print("""
    
    
    
    
    
    
    
    """)
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

def exit():
    num = input("按【Enter】键继续...")

def change():
    print('-' * 50)
    print("请选择需要修改的员工信息")
    print('')
    print('[1] ◆姓名修改◆')
    print('[2] ◆岗位修改◆')
    print('[3] ◆地点修改◆')
    print('[4] ◆时间修改◆')
    print('[5] ☹档案删除☹')
    print('[0] 返回')
    print('-' * 50)