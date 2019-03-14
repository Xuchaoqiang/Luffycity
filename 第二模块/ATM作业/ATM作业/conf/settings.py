#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

HANDLING_FEE = 0.05     # 提现手续费
DEFAULT_CREDIT = 15000  # 信用卡账户默认额度
# 创建用户时默认账户信息
DEFAULT_INFO = {'credit': 15000, 'cost_record': [], 'status': 0}

