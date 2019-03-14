#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'sohu': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {}
            },
            '上地': {
                '百度': {}
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {}
            },
            '天通苑': {
                '天通苑老男孩': {},
            },
            '回龙观': {
                '回龙观老男孩': {}
            }
        },
        '朝阳': {
            '小红门': {
                '小红门老男孩': {},
            },
            '十八里店': {
                '十八里店老男孩': {}
            }
        },
        '东城': {
            '东华门': {
                '东华门老男孩': {}
            },
            '永定门': {
                '永定门老男孩': {}
            }
        }
    },
    '上海': {
        '闵行': {
            '人民广场': {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {}
    },
    '山东': {}
}
current_menu = menu
old_menu = []
while True:
    for a in current_menu:
        print(a)
    choice = input('\033[33;1m 请输入您的选择(q:退出,b:返回上一层)： \033[0m').strip()
    if choice in current_menu:
        old_menu.append(current_menu)
        current_menu = current_menu[choice]
    elif choice == 'q': break
    elif choice == 'b':
        if old_menu:
            current_menu = old_menu.pop(-1)
    else:
        print('输入有误，请重新输入！')
