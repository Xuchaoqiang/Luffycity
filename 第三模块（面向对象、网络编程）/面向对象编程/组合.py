#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

class Weapon:
    def prick(self, obj):   # 这是该装备的主动技能， 扎死对方
        obj.life -= 500       # 假设攻击力为500

class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, life):
        self.name = name  # 每一个角色都有自己的昵称;
        self.weapon = Weapon()  # 给角色绑定一个武器;
        self.life = life

egg = Person('egon', 600)
p1 = Person('bb', 600)
egg.weapon.prick(p1)
print(p1.life)