#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# 一切皆文件
import abc      # 利用abc模块实现抽象类

class All_File(metaclass=abc.ABCMeta):
    all_type = 'file'
    @abc.abstractmethod
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod
    def write(self):
        '子类必须定义写功能'


class Txt(All_File):        # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法。')

    def write(self):
        print('文本数据的写入方法')


class Process(All_File): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')


class Sata(All_File):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('。。的读取方法。')

    def write(self):
        print('。。的写入方法')


wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

