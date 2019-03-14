#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# class Student:
#     school = 'luffycity'
#     count = 0
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         Student.count += 1
#
#     def learn(self):
#         print('%s learning..' % self.name)
#
# stu1 = Student('alex', 'male', 38)
# stu2 = Student('irving', 'male', 18)
# stu3 = Student('egon', 'female', 28)
#
# print(Student.count)
# print(stu1.count)


class Gaiwen:
    camp = 'Demacya'

    def __init__(self, name, life_value, power):
        self.name = name
        self.life_value = life_value
        self.power = power

    def attack(self, obj):
        obj.life_value -= self.power
        if obj.life_value < 0:
            print('%s is died!' % obj.name)


class Nuok:
    camp = 'nuoksic'

    def __init__(self, name, life_value, power):
        self.name = name
        self.life_value = life_value
        self.power = power

    def attack(self, obj):
        obj.life_value -= self.power
        if obj.life_value < 0:
            print('%s is died!' % obj.name)

g1 = Gaiwen('盖伦', 100, 20)
r1 = Nuok('瑞文', 80, 33)

r1.attack(g1)
r1.attack(g1)
r1.attack(g1)
r1.attack(g1)
print(g1.life_value)
