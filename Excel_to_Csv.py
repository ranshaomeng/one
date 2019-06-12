import pandas as pd
from pandas import Series,DataFrame
import datetime
import os
def count_time(func):
    def int_time():
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
    return int_time

@count_time
def xlsx_to_cvs_pd():
    for file in os.listdir(sourcePath):
        print(file)
       # print(name)
        filePath = os.path.join(sourcePath, file)
        #文件名用点分隔生成数组
        name=file.split(".")

        data_xls = pd.read_excel(filePath,index_col=1,sheet_name='附件2')
        print(type(data_xls))
        datas=pd.DataFrame(data_xls)
        print(type(datas))
        print(datas.head(10))
        datas.loc[5:10]
        print(outpath+name[0]+'.csv')
        data_xls.to_csv(outpath+name[0]+'.csv',encoding='gbk')

    #print(data_xls)
    #data_xls.to_json('dd.json')
sourcePath=r"D:\Python3.7.0\one\文件格式 转换\新建文件夹"
outpath=r"D:\Python3.7.0\one\文件格式 转换\\"
if __name__ == '__main__':
    xlsx_to_cvs_pd()