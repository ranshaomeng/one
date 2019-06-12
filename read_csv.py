#-*- coding:utf-8 -*-
import os
import pandas as pd
from pandas import Series,DataFrame
import datetime
import numpy as np
class GetInformation(object):


    def __init__(self, id):
        self.id = str(id)
        # print("id的数据类型")
        # print(type(id))
        # print(id)
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


def CBF_age():
    # df=DataFrame(pd.read_csv('d:\python3.7.0\code\CBF_JTCY2.csv',encoding='gbk',names=['cbfbm','cyxm','cyxb','cyzjlx','cyzjhm','yhzgx','cybz','sfgyr','cybzsm']))
    df = DataFrame(pd.read_csv('CBF.csv', encoding='gbk',
                               names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                      'o', ]))
    print(df.columns.values.tolist())
    print(df.describe())
    # 找空值付999，
    df['e'] = df['e'].fillna('999')
    #然后把999给删了
    df = df.drop(df[(df.e == '999')].index.tolist())
    # 做年龄结构分析
    # 根据身份证号的生日 添加年龄列
    df['age'] = df.apply(lambda x: GetInformation((x.e)).get_age(), axis=1)
    agegropts = pd.cut(df['age'], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, np.inf])
    print(agegropts)
    dss = pd.DataFrame(agegropts)  # 转成dataframe
    df['lei'] = dss['age']  # 添加 age列到df
    aa = df.groupby(['lei'])['c'].count()  # 以age透视 统计个数
    aa.to_csv('cbf_age1.csv')
    df.to_csv("df.csv",encoding='gbk')
    print(df['age'])

    print("ok")

#户的地块数量分布
def CBF_dikuai():
    # df=DataFrame(pd.read_csv('d:\python3.7.0\code\CBF_JTCY2.csv',encoding='gbk',names=['cbfbm','cyxm','cyxb','cyzjlx','cyzjhm','yhzgx','cybz','sfgyr','cybzsm']))
    df = DataFrame(pd.read_csv('abcd.csv',names=['CBHTBM', 'CBDKZS'],skiprows=1))
    print(df.columns.values.tolist())
    print(df.describe())
    print(df.dtypes)
    # 找空值付999，
    df['CBHTBM'] = df['CBHTBM'].fillna('999')
    dfd=df['CBDKZS']
    #dff=df['CBDKZS'].map(lambda  e:e.upper)
    # df['CBDKZS2']=df['CBDKZS'].astype(str)
    #print(df.dtypes)
    print(dfd)
    agegropts = pd.cut(df['CBDKZS'], [0, 10, 20, 30, 40])
    #df['分类']=agegropts['qe']
    print(type(agegropts))
    # df1=pd.DataFrame(df['YWLX'],dtype='int')
    # print(df1.dtypes)



    # print(df.head(10))
    # df['s']=df['CBDKZS'].astype(float)
   # print(df['CBFBM'])
    # 找空值付999，然后把999给删了
    # df['e'] = df['e'].fillna('999')
    # df = df.drop(df[(df.e == '999')].index.tolist())
    # # 做年龄结构分析
    # # 根据身份证号的生日 添加年龄列
    # df['age'] = df.apply(lambda x: GetInformation((x.e)).get_age(), axis=1)
    #agegropts = pd.cut(df['CBDKZS'], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, np.inf])
    #df['dksl'] = df.apply((x for x in df["CBDKZS"]))
    #print(pd.cut(float(df["CBDKZS"]),10))
        # dss = pd.DataFrame(agegropts)  # 转成dataframe
        # df['lei'] = dss['age']  # 添加 age列到df
        # aa = df.groupby(['lei'])['c'].count()  # 以age透视 统计个数
        # aa.to_csv('cbf_age.csv')
        # print("ok")



                # df=pd.DataFrame([[1,2,2],[1,4,5],[1,2,4],[1,6,3],[2,3,1],[2,4,1],[2,3,5],[3,1,1]],columns=['A','B','C'])
                # print(df)
                # agegropts = pd.cut(df['C'], [0, 3, 6,])
                #
                # print(agegropts)
                # dss=pd.DataFrame(agegropts)
                # df['D']=dss['C']
                # print(df)
                # DFFF=df.groupby(['D'])['C'].count()
                # DFFFS=df.groupby(['D'])
                # print(DFFF)
                # print([x for x in DFFFS])
CBF_dikuai()
#CBF_age()
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

