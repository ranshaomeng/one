from aip import AipOcr
import os
import sys

""" 你的 APPID AK SK """
APP_ID = '16044038'
API_KEY = 'dWaEmuTACtepKgAfx3uOylZ3'
SECRET_KEY = 'i2abuScoVn0z2hN30AoAvrmbVAnMnoZA'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
#文件夹路径
paths=r"D:\Python3.7.0\baidu\aa\新建文件夹"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#输出的txt文件
data=open(r'D:\Python3.7.0\baidu\aa\1.txt','r+')
for file in os.listdir(paths):
     #print(file)

    image = get_file_content(paths+"\\"+file)

    """ 调用通用文字识别, 图片参数为本地图片 """
    client.basicGeneral(image, 0);

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    options["result_num"] = 30
    options["result"] = [5, 6]
    options["log_id"] = "1"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    result = client.basicGeneral(image, options)
    words_result = result['words_result']
    for i in range(len(words_result)):
        #print(words_result[i]['words'])
        aa=words_result[i]['words']
        print(str(aa)+"\n")
        data.write(aa+"\n")


