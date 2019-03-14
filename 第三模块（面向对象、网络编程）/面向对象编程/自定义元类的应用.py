#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# 单类模式

class Mymeta(type):
    def __init__(self, class_name, class_basses, class_dic):
        super(Mymeta, self).__init__(class_name, class_basses, class_dic)

        self.__instance = None

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            obj = object.__new__(self)
            self.__init__(obj)
            self.__instance = obj

        return self.__instance

class Mysql(object, metaclass=Mymeta):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306


obj1=Mysql()
obj2=Mysql()
obj3=Mysql()

print(obj1 is obj2 is obj3)