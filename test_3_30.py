'''
 Name: 模拟自动取款机
 Description: 数据临时存放在变量列表中，实现一个取款机上的存取款
              模拟效果，包括登录、退出、查询余额、取款和存款功能
'''

# 账号信息列表
accoutList = [{'accout': '202114060411', 'name': 'Sunwen', 'passwd': '123456', 'balance': 10000.00},
              {'accout': '202114060404', 'name': 'Gaofeng', 'passwd': '654321', 'balance': 10000.00},
              {'accout': '202114060425', 'name': 'Chengxing', 'passwd': 'return', 'balance': 20000.00},
              {'accout': '202114060426', 'name': 'Lisa', 'passwd': 'myoffer', 'balance': 40000.00}]


# 进入管理员系统，显示所有账户信息
def showAccout(accout, passwd, accoutList):
    if accout == "1" and passwd == "1":
        if len(accoutList) == 0:
            print("(I) No Data from Accout")
            return
        print("|{0:<10} | {1:<10} | {2:<10} | {3:<10}".format("accout",
                                                              "name", "passwd", "balance"))
        print("-" * 40)
        for i in range(len(accoutList)):
            print("|{0:<10} | {1:<10} | {2:<10} | {3:<10}".format(accoutList[i]['accout'],
                                                                  accoutList[i]['name'], "******",
                                                                  accoutList[i]['balance']))
        print("")
        input("按回车键退出管理员系统：")
        return
    else:
        return None


# 登录界面
def showLoginPage():
    print("+-------------------------------+")
    print("+                               +")
    print("+              ATM              +")
    print("+                               +")
    print("+-------------------------------+")
    print("            （请插卡）           ")


# 验证账号及密码
def checkAccout(accout, passwd):
    for i in range(len(accoutList)):
        if accout == accoutList[i]['accout'] and passwd == accoutList[i]['passwd']:
            return i
    # 没有匹配成功
    return -1


# 初始化界面
def showMainPage():
    print("")
    print("=" * 13, "自动存取款系统", "=" * 13)
    print("{0:1} {1:13} {2:15}".format(" ", "1.查询",
                                       "2.取款"))
    print("{0:1} {1:13} {2:15}".format(" ", "3.存款",
                                       "4.退出系统"))
    print("=" * 42)


# 自动取款机业务
def atmService(index):
    key = input("请输入对应的选择：")
    print("")
    if key == "1":
        print("=" * 14, "查询账户余额", "=" * 14)
        # showAccout(accoutList)
        print("> 账户姓名：", accoutList[index]['name'])
        print("> 当前账户：", accoutList[index]['accout'])
        print("> 当前余额：", accoutList[index]['balance'], end='\n\n')
        return 0

    elif key == "2":
        print("=" * 14, "取款", "=" * 14)
        money = input("请输入取款金额（元）：￥")
        if int(money) > 0 and int(money) <= accoutList[index]['balance']:
            accoutList[index]['balance'] -= int(money)
            print("> 取款成功！*^_^*")
            print("> 当前余额：", accoutList[index]['balance'], end='\n\n')
            print("(I) 请取走现金并妥善保管")
            return 0
        else:
            print("(E) 余额不足，取款失败")
            return -1

    elif key == "3":
        print("=" * 14, "存款", "=" * 14)
        money = input("> 存入金额（元）：￥")
        accoutList[index]['balance'] += int(money)
        print("> 存款成功！*^_^*")
        print("> 当前余额：", accoutList[index]['balance'], end='\n\n')
        return 0

    elif key == "4":
        print("=" * 18, "再见", "=" * 18)
        return 1
    else:
        print("Try again!")
        return -1


# 开始啦
showLoginPage()
accout = input("请输入账号：")
passwd = input("请输入密码：")
showAccout(accout, passwd, accoutList)
index = checkAccout(accout, passwd)
if index >= 0:
    print("(I) 登录成功")
    while True:
        showMainPage()
        if 1 == atmService(index):
            break
        input("按回车键继续：")
else:
    print("(I) 登录失败，请检查账号和密码")
