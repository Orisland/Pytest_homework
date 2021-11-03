import operator
from filecmp import cmp

import xlrd
import mysql

"""
author:zhaolong
date:2021年11月02日22:04:34
"""

data = xlrd.open_workbook("/Users/zhaolong/Downloads/test.xlsx")
table = data.sheets()[0]
nrows = table.nrows
list = []

for i in range(1,nrows):
    temp = []
    for j in range(table.ncols):
        temp.append(table.cell_value(i, j))
    list.append(temp)

for t in list:
    temp = mysql.find(t[0])
    print(temp)
    print(t)
    if temp is None:
        mysql.insert(t[0], t[1], t[2], t[3], xlrd.xldate_as_datetime(t[4], datemode=0).strftime("%Y-%m-%d"))
        continue
    if operator.eq(t, temp) is False:
        mysql.update(t[1], t[2], t[3], xlrd.xldate_as_datetime(t[4], datemode=0).strftime("%Y-%m-%d"), t[0])

