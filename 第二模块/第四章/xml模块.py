#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import xml.etree.ElementTree as ET

tree = ET.parse('xml_data')     # 打开文件句柄

root = tree.getroot()       # 获取xml文件的根节点   f.seek()

print(root.tag)

# 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)

# 只遍历 某个节点
# for node in root.iter('year'):
#     print(node.tag, node.text)

# 修改和删除xml文档内容
# 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set('update', 'yes')   # 设置attrib
#
# tree.write('xml_data')

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

