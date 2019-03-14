#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import zipfile
# 压缩
# z = zipfile.ZipFile('test.zip', 'w')
# z.write('my_proj')
# z.write('shutil_new')
# z.close()

# 解压
# z = zipfile.ZipFile('test.zip', 'r')
# z.extractall('my_proj')
# z.close()

import tarfile

# 压缩
# t = tarfile.open('tar_test.tar', 'w')
# t.add('shuti_new2')
# t.close()

# 解压
t = tarfile.open('tar_test.tar', 'r')
t.extractall('tar_test')
t.close()