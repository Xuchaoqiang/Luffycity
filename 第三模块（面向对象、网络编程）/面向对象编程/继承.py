#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

class Role:
    def __init__(self, name, life_value, power):
        self.name = name
        self.life_value = life_value
        self.power = power

    def attack(self, obj):
        obj.life_value -= self.power
        if obj.life_value < 0:
            print('%s is died!' % obj.name)


class Gaiwen(Role):
    camp = 'Demacya'


class Nuok(Role):
    camp = 'nuoksic'


g1 = Gaiwen('盖伦', 100, 20)
r1 = Nuok('瑞文', 80, 33)

r1.attack(g1)
r1.attack(g1)
r1.attack(g1)
r1.attack(g1)
print(g1.life_value)
