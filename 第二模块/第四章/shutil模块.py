#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# 高级的 文件、文件夹、压缩包 处理模块

import shutil

# 将文件内容拷贝到另一个文件中, 需要手段open
# shutil.copyfileobj(open('shutil模块.py', 'r', encoding='utf-8'), open('shutil_new', 'w', encoding='utf-8'))

# 拷贝文件，简短版, 不用手动open
# shutil.copyfile('shutil模块.py', 'shuti_new2')

# shutil.copymode       #仅拷贝权限

# shutil.copystat       #仅拷贝状态信息

# shutil copy       #拷贝文件和权限

# shutil copy2      #拷贝文件和状态信息

# shutil.copytree     #递归的去拷贝文件夹
# shutil.copytree('my_proj', 'p3', ignore=shutil.ignore_patterns('__init__.py'))

# shutil.move       #递归的去移动文件，类似mv
# shutil.move('p3', 'p5')

# shutil.rmtree         #递归的去删除文件
# shutil.rmtree('p5')

# shutil.make_archive()     创建压缩包并返回文件路径
# shutil.make_archive('data_bak', 'gztar', root_dir='my_proj')

# shutil 对压缩包的处理是调用 ZipFile 和 Tarfile来进行的

