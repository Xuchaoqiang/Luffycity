#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

class Person:   # 定义一个人类
    role = 'person'     # 人的属性都是人
    def __init__(self, name, life_value, aggressivity):
        self.name = name    # 每一个角色都有自己的名称
        self.life_value = life_value    # 每一个角色都有自己的生命值
        self.aggressivity = aggressivity    # 每一个角色都有自己的攻击力

    def attack(self, dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.aggressivity


class Dog:      # 定义一个狗类
    role = 'dog'    # 狗的属性就是狗
    def __init__(self, name, life_value, aggressivity):
        self.name = name    # 每个狗都有自己的名字
        self.life_value = life_value    # 每个狗都有自己的生命值
        self.aggressivity = aggressivity       # 每个狗都有自己的攻击力

    def attack(self, person):
        person.life_value -= self.aggressivity

# 实例化一个人
p1 = Person('alex', 100, 20)
# 实例化一个狗
d1 = Dog('eee', 80, 50)

# 狗去攻击人
d1.attack(p1)
print(p1.life_value)
