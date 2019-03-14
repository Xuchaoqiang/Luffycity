#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import time
from core import db_handler
from conf import settings
from core import auth
from core import logger

MENU = """
1.  提现
2.  转账
3.  还款
4.  查看流水"""
HANDLING_FEE = settings.HANDLING_FEE        # 提现手续费
DEFAULT_CREDIT = settings.DEFAULT_CREDIT    # 默认额度
user_data = auth.user_data      # 用户认证装饰器返回的用户数据

@auth.auth_login
def with_draw():
    """
    用户提现功能函数
    :return:
    """
    data = user_data[0]     # user_data里面只会存在一个元素是字典，字典里才是用户数据
    user_credit = data['credit']    # 用户信用卡额度
    print('您的额度为：%s' % user_credit)
    amount = input('请输入要提现的金额：').strip()
    if amount.isdigit():
        choice = int(amount)
        if choice <= user_credit:
            data['credit'] = user_credit - choice*(1+HANDLING_FEE)
            # 流水记录  因为流水记录直接写入用户json文件，所以用户变动后的数据在 cost_record函数里面 save_db
            cost_record('withdraw', amount, data)
            # 日志记录
            logger.logger.info('{0} withdraw ${1}'.format(data['id'], choice))
            print('提现成功！您的额度还剩下：%s' % data['credit'])
        else:
            print('\033[31;1m 您的额度不足，请重新输入！ \033[0m')
    else:
        print('\033[31;1m Inval values！ \033[0m')

@auth.auth_login
def transfer():
    """
    用户转账功能函数
    :return:
    """
    target = input('请输入收款方姓名：').strip()
    source_data = user_data[0]
    target_data = db_handler.load_db(target)
    source_credit = source_data['credit']       # 原账户额度
    target_credit = target_data['credit']       # 对方账户额度
    amount = input('请输入要转账的金额：').strip()
    if amount.isdigit():
        amount = int(amount)
        if amount <= source_credit:
            amount = int(amount)
            target_data['credit'] = target_credit + amount
            db_handler.save_db(source_data['id'], source_data)
            db_handler.save_db(target, target_data)
            # 流水记录
            cost_record('transfer to %s' % target, amount, source_data)
            # 日志记录
            logger.logger.info('{0} transfer to {1} ${2}'.format(source_data['id'], target, amount))
            print('转账成功！')
        else:
            print('\033[31;1m 您的额度不够！无法完成转账。\033[0m')
    else:
        print('\033[31;1m Inval values！ \033[0m')

@auth.auth_login
def shopping_cost(cost):
    """
    购物商场付款接口
    :param cost: 消费金额
    :return:
    """
    data = user_data[0]
    user_credit = data['credit']       # 用户信用卡额度
    if cost > user_credit:
        print('\033[31;1m 您的额度不足，无法完成此次购物。\033[0m')
    else:
        data['credit'] = user_credit - cost
        # 流水记录
        cost_record('shopping_cost', cost, data)
        # 日志记录
        logger.logger.info('{0} shopping_cost ${1}'.format(data['id'], cost))
        print('\033[33;1m 消费成功，您的账户余额为：%s元\033[0m' % data['credit'])

@auth.auth_login
def repayment():
    """
    用户还款接口
    :return:
    """
    data = user_data[0]
    user_credit = data['credit']
    print('当前账户额度为：%s' % user_credit)
    if user_credit < DEFAULT_CREDIT:
        repay = input('请输入还款金额：').strip()
        if repay.isdigit() and int(repay) > 0:
            repay = int(repay)
            data['credit'] = user_credit + repay
            # 流水记录
            cost_record('repayment', repay, data)
            # 日志记录
            logger.logger.info('{0} repayment ${1}'.format(data['id'], repay))
            print('{0} 还款成功， 目前额度为{1}元。'.format(data['id'], data['credit']))
        else:
            print('\033[31;1m Invaild values! \033[0m')
    else:
        print('\033[33;1m 您无需还款。\033[0m')

def cost_record(*args, **kwargs):
    """
    用户记录流水函数， 涉及到记录流水的，数据都会留到此函数最后才更改用户数据 save_db
    :param args:
    :param kwargs:
    :return:
    """
    record = '{0} <{1}>  $:{2}'.format(time.ctime(), args[0], args[1])
    data = args[2]
    data['cost_record'].append(record)      # 把流水记录加到用户数据文件json里面
    db_handler.save_db(data['id'], data)

@auth.auth_login
def view_record():
    """
    查看用户流水记录接口
    :return:
    """
    data = user_data[0]
    for i in data['cost_record']:
        print(i)
    # 记录日志
    logger.logger.info('{0} view_record'.format(data['id']))

def run():
    """
    入口启动函数
    :return:
    """
    while True:
        print(MENU)
        choice = input('请选择 >>:').strip()
        if choice == '1':
            with_draw()
        elif choice == '2':
            transfer()
        elif choice == '3':
            repayment()
        elif choice == '4':
            view_record()
        else:
            print('\033[31;1m Invaild values! \033[0m')

