#-*- coding:utf-8 -*-
#第一稿 留记录
import os
import pandas as pd
from pandas import Series,DataFrame
import datetime
import numpy as np

df=DataFrame(pd.read_csv('d:\python3.7.0\code\CBF_JTCY2.csv',encoding='gbk',names=['cbfbm','cyxm','cyxb','cyzjlx','cyzjhm','yhzgx','cybz','sfgyr','cybzsm']))
print(df.describe())

class GetInformation(object):


    def __init__(self, id):
        self.id = str(id)
        print("id的数据类型")
        print(type(id))
        print(id)
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_birthday(self):
        """通过身份证号获取出生日期"""
        birthday = "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)
        return birthday

    def get_sex(self):
        """男生：1 女生：2"""
        num = int(self.id[16:17])
        if num % 2 == 0:
            return 2
        else:
            return 1

    def get_age(self):
        """通过身份证号获取年龄"""
        now = (datetime.datetime.now() + datetime.timedelta(days=1))
        year = now.year
        month = now.month
        day = now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year


aa=230121194306060611
print(type(aa))

df['cyzjhm']=df['cyzjhm'].fillna('999')
df=df.drop(df[(df.cyzjhm=='999')].index.tolist())

df['age']=df.apply(lambda x:GetInformation((x.cyzjhm)).get_age(),axis=1)
#
# print(df.dtypes)
# # print(df.index.values)
# # print(df.columns.values.tolist())
# # print(df)
print(df.describe())
#df.to_csv('ok1.csv')
# bins=4
# bins=[5,50,60,np.inf]
agegropts=pd.cut(df['age'],[0,10,20,30,40,50,60,70,80,90,100,110,120,np.inf])
#print(agegropts.columns.values.tolist())
print(type(agegropts))
#agegropts.to_csv('ok.csv')
dss=pd.DataFrame(agegropts)
print(type(dss))
print(dss.columns.values.tolist())
print(dss)
dss['c']=dss['age']
#aaa=dss.groupby(['age'])['c'].sum()
print(dss)
# df3=df.groupby(agegropts).mean()
aa=dss.groupby(['age'])['c'].count()
aa.to_csv('ok_4.csv')
