#!-*- coding:utf-8 -*-
#__author__:"irving"

import sys
import os
# 程序入口，调整python环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from core import manager_handler


if __name__ == '__main__':
    manager_handler.run()


