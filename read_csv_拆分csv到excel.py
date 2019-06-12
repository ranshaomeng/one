#-*- coding:utf-8 -*-
import os
import pandas as pd
from pandas import Series,DataFrame
import datetime
import numpy as np


#df=DataFrame(pd.read_csv('d:\python3.7.0\code\CBF_JTCY2.csv',encoding='gbk',names=['cbfbm','cyxm','cyxb','cyzjlx','cyzjhm','yhzgx','cybz','sfgyr','cybzsm']))
#df=DataFrame(pd.read_csv(r'D:\2019年土地承包处\农村承包地确权登记表（全国）\整理基础数据—秘书局数据来源\数据统计整理20190521\统计结果整理4期-张寅\2715+123数据\动态\123个县未汇交数据\123个县（地方确认表整合）.csv',encoding='gbk',names=['XH','ZBMS','HJSZ','JBSZ','QRSZ','BZ','YWLX','QSDWDM','QSDWMC']))
df=DataFrame(pd.read_csv('123表.csv',encoding='utf-8'))

print(df.columns.values.tolist())
print(df.describe())
# 找空值付999，然后把999给删了
# df['e']=df['e'].fillna('999')
# df=df.drop(df[(df.e=='999')].index.tolist())
# # 做年龄结构分析
# #根据身份证号的生日 添加年龄列
# df['age']=df.apply(lambda x:GetInformation((x.e)).get_age(),axis=1)
# agegropts=pd.cut(df['age'],[0,10,20,30,40,50,60,70,80,90,100,110,120,np.inf])
# dss=pd.DataFrame(agegropts) #转成dataframe
# df['lei']=dss['age'] #添加 age列到df
# aa=df.groupby(['lei'])['c'].count()#以age透视 统计个数
# aa.to_csv('cbf_age.csv')
# print("ok")

#做性别结构分析
# df['sex']=df.apply(lambda x:GetInformation((x.cyzjhm)).get_sex(),axis=1)
# print(df)
# aa=df.groupby((['sex']))['cyxb'].count()
# bb=df.groupby((['cyxb']))['sex'].count()
# print(aa)
# print(bb)

#承包包 分为户主（02）和本人（01）
# aa=df[(df.yhzgx == 1) | (df.yhzgx == 2)]
# print(aa.describe())
# bb=df[(df.yhzgx == 1) ]
# print(bb.describe())
# cc=df[(df.yhzgx == 2) ]
# print(cc.describe())


#print(df.groupby(agegropts).mean())

#
# df8=pd.merge(df,dss,on='index')
# print(df8)

# dss['c']=dss['age']
# aa=dss.groupby(['age'])['c'].count()
# aa.to_csv('ok3.csv')


# print(df.describe())
# df.to_csv('ok1.csv')
# bins=4
# bins=[5,50,60,np.inf]
#根据年龄分组

#print(agegropts.columns.values.tolist())
#agegropts.to_csv('ok2.csv')

# print(type(dss))
# print(dss.columns.values.tolist())
# print(dss)

#aaa=dss.groupby(['age'])['c'].sum()
# print(dss)
# df3=df.groupby(agegropts).mean()

