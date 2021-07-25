# Personnel_Management_System
PMS人员管理系统V3.1

因为要通过Pymysql库调用Mysql语句来实现对数据库内的增删改查，导致原先的代码全部得重构。。。
花了10个小时把300行代码重构到了1000多行，框架进行了模块化修改。
别问，问就是增加了可读性和可维护性
考虑到后期维护，tools.py函数包分割成menu，join，search，change，progress五个模块，还加了个进度条
