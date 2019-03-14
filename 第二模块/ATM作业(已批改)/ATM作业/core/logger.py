#!-*- coding:utf-8 -*-
#__author__:"irving"

import logging
from conf import settings
BASE_DIR = settings.BASE_DIR
ATM_LOG = BASE_DIR + r"\logs\atm.log"
ADMIN_LOG = BASE_DIR + r"\logs\admin.log"

# 定义logger（ATM操作），提供调用接口
logger = logging.Logger('ATM')
logger.setLevel(logging.INFO)
# 定义handler， 指定输出目的地
ch = logging.StreamHandler()
fh = logging.FileHandler(ATM_LOG)
# 定义formatter, 指定输出格式
formatter = logging.Formatter('%(asctime)s  - %(levelname)s  %(message)s')
# 给handler指定 set formatter
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# 给logger 绑定 handler  add
logger.addHandler(fh)
# logger.addHandler(ch)


# 定义ad_logger（admin操作），提供调用接口
ad_logger = logging.Logger('ADMIN')
ad_logger.setLevel(logging.INFO)
# 定义handler， 指定输出目的地
ad_ch = logging.StreamHandler()
ad_fh = logging.FileHandler(ADMIN_LOG)
# 定义formatter, 指定输出格式
ad_formatter = logging.Formatter('%(asctime)s  - %(levelname)s  %(message)s')
# 给handler指定 set formatter
ad_ch.setFormatter(ad_formatter)
ad_fh.setFormatter(ad_formatter)
# 给logger 绑定 handler  add
ad_logger.addHandler(ad_fh)
# ad_logger.addHandler(ad_ch)

