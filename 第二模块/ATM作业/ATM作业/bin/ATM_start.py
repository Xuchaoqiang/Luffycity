#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import sys
# 程序入口，调整python环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from core import main

if __name__ == '__main__':
    main.run()

