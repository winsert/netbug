#!/usr/bin/env python
# -*- coding: UTF-8 -*-
## 对*.json文件进行验证

import json

filename = raw_input("请输入文件名(*.json):")

jf = open(filename, 'r')

data = json.loads(jf.read())

print data
print

for x, y in data.items():
    print x, y

jf.close()
