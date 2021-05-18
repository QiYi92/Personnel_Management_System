import sys
import time


def progress_bar():
    for i in range(1, 101):  # 100%
        print("\r", end="")
        print("PMS程序启动中: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.01)
    print("complete")

    for i1 in range(1, 101):  # 100%
        print("\r", end="")
        print("数据库连接中:  {}%: ".format(i1), "▋" * (i1 // 2), end="")
        sys.stdout.flush()
        time.sleep(0.005)
    print("complete")

    for i2 in range(1, 101):  # 100%
        print("\r", end="")
        print("维护模块加载中: {}%: ".format(i2), "▋" * (i2 // 2), end="")
        sys.stdout.flush()
        time.sleep(0.0005)
    print("complete")

    for i3 in range(1, 101):  # 100%
        print("\r", end="")
        print("查询模块加载中: {}%: ".format(i3), "▋" * (i3 // 2), end="")
        sys.stdout.flush()
        time.sleep(0.0005)
    print("complete")

    for i4 in range(1, 101):  # 100%
        print("\r", end="")
        print("删除模块加载中: {}%: ".format(i4), "▋" * (i4 // 2), end="")
        sys.stdout.flush()
        time.sleep(0.0005)
    print("complete")

    for i5 in range(1, 101):  # 100%
        print("\r", end="")
        print("进行数据校对:  {}%: ".format(i5), "▋" * (i5 // 2), end="")
        sys.stdout.flush()
        time.sleep(0.002)
    print("complete")

    print("一切准备就绪(～￣▽￣)～ ")