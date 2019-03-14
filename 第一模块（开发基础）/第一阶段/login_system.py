#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import getpass

#存放用户信息的字典
user_info = {'alex': '123', 'egon': '123456', 'irving': '111'}

#功能菜单
message_info = '''
a.登陆
b.退出系统
'''

#第一层loop，可以让用户选择功能
while True:
    print(message_info)
    choice = input('please input your choice:').strip()
    if choice == 'a':
        username = input('please enter your name:').strip()
        #输入用户名之后需要验证用户是否是block状态，'block_user'文件需要事先创建好。
        if username in user_info:
            f = open('block_user', 'r')
            #因为存入的block user后面会带\n， 所以要去掉才能进行判断
            f_user = []
            for line in f.readlines():
                f_user.append(line.strip())
            #print(f_user)

            f.close()
            if username not in f_user:
                #第二次loop，3次验证失败后退出程序
                count = 3
                while count > 0:
                    count -= 1
                    password = input('please input your password:').strip()
                    if user_info[username] == password:
                        print('\033[32;1m welcome %s\033[0m' % username)
                        break
                    else:
                        print('\033[31;1m your password is not match, you have %d chance.\033[0m' % count)
                    # 用户输入错误三次之后，存入block_user文件
                    if count == 0:
                        print('\033[31;1m user %s is blcoking.\033[0m' % username)
                        f = open('block_user', 'a')
                        f.write(username+'\n')
                        f.close()
            else:
                print('\033[31;1m %s is blocking!\033[0m' %username)
        else:
            print('\033[31;1m the user is not exist!\033[0m')

    elif choice == 'b':
        break
    else:
        print('\033[31;1m command not exist! \033[0m')