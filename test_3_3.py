def get_all_students():
    students = []
    f = open('s_list.txt')
    for line in f:
        line = line.replace('\n', '')
        student = line.split(' ')
        students.append(student)
    f.close()
    return students


def add_student():  # 添加学生信息
    students = get_all_students()
    id = input('学号: ')
    for i in range(len(students)):
        if (students[i][0] == id):#判断是否存在该学号的学生信息
            print('该学号的学生信息已存在,请重新输入！')
            add_student()
            login()

    name = input('姓名: ')
    sex = input('性别: ')
    age = input('年龄: ')
    grade_class = input('班级: ')
    major = input('专业: ')
    college = input('学院: ')
    phone_number = input('电话号码: ')

    students.append([id, name, sex, age, grade_class, major, college, phone_number])

    f = open('s_list.txt', 'w')
    for i in range(len(students)):
        student = ' '.join(students[i]) + '\n'
        f.write(student)
    f.close()
    print('学生记录添加成功！')


def disaplay_all_students():  # 查询所有学生信息
    students = get_all_students()
    for i in range(len(students)):
        for j in range(len(students[i])):
            print(students[i][j], end=' ')
        print()


def id_disaplay_student():  # 以学号查询学生信息
    id = input('学号: ')
    found = False
    students = get_all_students()
    for i in range(len(students)):
        if (students[i][0] == id):
            found = True
            for j in range(len(students[i])):
                print(students[i][j], end=' ')
            break
    if not found:
        print(f'学生信息中没有学号为{id}的学生！')


def name_disaply_student():  # 以姓名查询学生信息
    name = input('姓名: ')
    students = get_all_students()
    found = False
    for i in range(len(students)):
        if (students[i][1] == name):
            found = True
            for j in range(len(students[i])):
                print(students[i][j], end=' ')
            break
    if not found:
        print(f'学生信息中没有姓名为{name}的学生！')


def query_student():  # 查询学生记录
    while True:
        print('\n查询学生记录\n')
        print('=================')
        print('1.按学号查询学生记录')
        print('2.按姓名查询学生记录')
        print('3.查询全部学生记录')
        print('4.返回上级菜单')
        print('=================')
        mc3 = int(input('输入菜单号：'))
        if mc3 == 1:
            id_disaplay_student()
        elif mc3 == 2:
            name_disaply_student()
        elif mc3 == 3:
            disaplay_all_students()
        else:
            break


def modify_student():  # 修改学生信息
    students = get_all_students()
    id = input('需要修改信息的学生的学号: ')
    new_name = input('姓名: ')
    new_sex = input('性别: ')
    new_age = input('年龄: ')
    new_grade_class = input('班级: ')
    new_major = input('专业: ')
    new_college = input('学院: ')
    new_phone_number = input('电话号码: ')

    found = False
    for i in range(len(students)):
        if (students[i][0] == id):
            found = True
            students[i][1] = new_name
            students[i][2] = new_sex
            students[i][3] = new_age
            students[i][4] = new_grade_class
            students[i][5] = new_major
            students[i][6] = new_college
            students[i][7] = new_phone_number
            print('修改成功！')
            for j in range(len(students[i])):
                print(students[i][j], end=' ')
            break
    if not found:
        print(f'学生信息中没有学号为{id}的学生！')

    f = open('s_list.txt', 'w')
    for i in range(len(students)):
        student = ' '.join(students[i]) + '\n'
        f.write(student)
    f.close()


def delete_student():
    students = get_all_students()
    id = input('输入要删除信息的学生的学号:')
    found = False
    for i in range(len(students)):
        if (students[i][0] == id):
            found = True
            break
    if not found:
        print(f'学生信息中没有学号为{id}的学生！')
    else:
        del students[i]
        print(f'学号为{id}的信息已成功删除！')
    f = open('s_list.txt', 'w')
    for i in range(len(students)):
        student = ' '.join(students[i]) + '\n'
        f.write(student)
    f.close()


def login():
        while True:
            print('\n学生信息管理系统')
            print('=============')
            print('1. 添加学生记录')
            print('2. 查询学生记录')
            print('3. 修改学生记录')
            print('4. 删除学生记录')
            print('5. 退出管理系统')
            print('=============')
            mc2 = int(input('输入菜单号: '))
            if mc2 == 1:
                add_student()
            elif mc2 == 2:
                query_student()
            elif mc2 == 3:
                modify_student()
            elif mc2 == 4:
                delete_student()
            else:
                break


# 主程序
while True:
    login()
    print('已退出')
    break
