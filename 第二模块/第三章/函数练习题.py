#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

user_info = []      # 把account.txt转成一个嵌套列表，每个子列表存着每个账户的信息。  被global
person_info = []    # 列表里面存着登陆用户的信息。    被global
login_status = False        # 登陆状态码

menu = '''
    1.修改个人信息
    2.打印个人信息
    3.修改密码
    4.退出程序'''       # 功能主菜单

def file_IO(mode):
    '''
    文件(account.txt)读写函数
    :param mode:'r'为读文件，'w'为写文件
    :return:
    '''
    if mode is 'r':
        with open('account.txt', 'r', encoding='utf-8') as f:
            for line in f:
                person_data = []
                info_list = line.split(',')
                for i in info_list:
                    person_data.append(i.strip())
                user_info.append(person_data)
    elif mode is 'w':
        with open('account.txt', 'w', encoding='utf-8') as f:
            for i in user_info:
                f.write(','.join(i))
                f.write('\n')
                f.flush()

def login():
    '''
    用户登陆模块
    :return:
    '''
    file_IO('r')
    count = 3       # 计数器，限制错误次数。
    global login_status     #把login_status global了，用来判断用户登陆状态，True即退出循环。
    while not login_status:
        username = input('Input your account:').strip()
        if not username:
            print('用户名不能为空！')
            continue
        passwd = input('Input your password:').strip()
        if not passwd:
            print('密码不能为空！')
            continue
        for i in user_info:
            if username == i[0] and passwd == i[1]:
                # 这里person_info也global了，因为需要直接对其进行赋值（引用'user_info'的子列表），修改的时候只需要把
                # user_info重新写入文件就OK
                global person_info
                person_info = i
                login_status = True
        if login_status == False:
            print('\033[31;1m 账号密码错误，请重新输入！\033[0m')
        if count == 1:
            exit()
        count -= 1

def change_info():
    print('person data:', person_info)
    person_data = '''
2. Name:{0}
3. Age:{1}
4. Job:{2}
5. Dept:{3}
6. Phone:{4}'''.format(person_info[2], person_info[3], person_info[4], person_info[5], person_info[6])
    print(person_data)
    choice = input('select column id to change:').strip()
    if not choice:
        print('选择不能为空。')
    elif int(choice):
        choice = int(choice)
        if choice <= len(user_info) and choice >= 2:
            print('current value >: ', person_info[choice])
            new_choice = input('new_value>:').strip()
            person_info[choice] = new_choice
            print('modify successfully! new info>: ', person_info)
            file_IO('w')
    else:
        print('\033[31;1m please input a valid value! \033[0m')

def review_info():
    person_data = '''
    ----------------
    Name:   {}
    Age:    {}
    Job:    {}
    Dept:   {}
    Phone:  {}
    -----------------
    '''.format(person_info[2], person_info[3], person_info[4], person_info[5], person_info[6])
    print(person_data)

def change_passwd():
    print('person data: ', person_info)
    new_passwd = input('please input your new password:'.strip())
    person_info[1] = new_passwd
    print('\033[32;1m Change password successfully! \033[0m')
    file_IO('w')

if __name__=='__main__':
    login()
    if login_status == True:
        while True:
            print(menu)
            function_dict = {1: change_info, 2: review_info, 3: change_passwd}
            choice = input('input your choice:').strip()
            if not choice:
                print('选择不能为空。')
            elif int(choice):
                choice = int(choice)
                if choice == 4:
                    break
                function_dict.get(choice)()
            else:
                print('\033[31;1m please input a valid value! \033[0m')
