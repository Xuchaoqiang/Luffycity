#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
import sys,os
# from ..crm import modules
from . import modules

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

print(sys.path[-1])


from proj import  settings

settings.setting()

def view():
    print('in the views!')
