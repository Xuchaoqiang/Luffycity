#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        update_dic = {}
        for i,v in enumerate(class_dic):
            if not callable(v) and not i.startwith('__'):
                update_dic[i.upper()] = v
            else:
                update_dic[i] = v

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)
        return type.__new__(self, class_name, class_bases, update_dic)

class People(object, metaclass=Mymeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walking(self):
        print('walking...')

    def talking(self):
        print('talking...')

print(People.__dict__)