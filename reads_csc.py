# 先将.xls文件导出成.csv文件
# 注意：以下一切代码均为英文输入法，包括标点符号等！！

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas
# numpy：科学计算工具包
# pandas：数据分析工具包
# malplotlib：图表绘制工具包
# improt语句：加载工具包

#data = pd.read_csv("D:\\Python3.7.0\\data\\地市级党委书记数据库（2000-10）.csv",encoding = "gbk",engine = 'python')
data = pandas.read_csv("D:\\Python3.7.0\\data\\data.csv",encoding = "utf-8",engine = 'python')
#print(data)
#print(data[10:40])
#print(data.head(15))
fileld=data.columns
print(fileld)
# 加载csv数据，并且将数据赋予data变量
# 这里用到了pandas的工具包，读取数据之后的格式为Dataframe，是一种矩阵格式（execl的数据表格其实也是一种矩阵格式）
# pyhton中，创造一个变量的方法就是给其赋值，而“=”代表 变量赋值
# print()是python最基本的语句之一，代表“打印内容”

# 注意，对于读取文件报错情况，可尝试以下方法：
# ① excel转csv时，可设置编码为utf-8，并更改参数 → encoding = 'utf-8'
# ② mac导出csv时，可以更改参数 → encoding = "gb18030"
# ③ 可将文件名改为英文文件名，例如“data.csv”