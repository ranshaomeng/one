# -*- coding:utf-8 -*-

import requests
from PIL import Image,ImageDraw,ImageFont
import glob
from datetime import datetime
import os.path
import json

def exifread_infos(photo):
        import exifread
        # 加载 ExifRead 第三方库  https://pypi.org/project/ExifRead/
        # 获取照片时间、经纬度信息
        # photo参数：照片文件路径

        # Open image file for reading (binary mode)
        f = open(photo, 'rb')
        # Return Exif tags
        tags = exifread.process_file(f)

        try:
            # 拍摄时间
            EXIF_Date = tags["EXIF DateTimeOriginal"].printable
            # 纬度
            LatRef = tags["GPS GPSLatitudeRef"].printable
            Lat = tags["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            Lat = float(Lat[0]) + float(Lat[1]) / 60 + float(Lat[2]) / float(Lat[3]) / 3600
            if LatRef != "N":
                Lat = Lat * (-1)
            # 经度
            LonRef = tags["GPS GPSLongitudeRef"].printable
            Lon = tags["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            Lon = float(Lon[0]) + float(Lon[1]) / 60 + float(Lon[2]) / float(Lon[3]) / 3600
            if LonRef != "E":
                Lon = Lon * (-1)
            f.close()
        except:
            return "ERROR:请确保照片包含经纬度等EXIF信息。"
        else:
            return EXIF_Date, Lat, Lon
def add_num(pattern,texts,outpath):
    setFont = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', 100)
    fillColor = "#DC143C"

    for img in glob.glob(pattern):
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        width, height = image.size
       # draw.text((image.size[0] / 10, image.size[1]-image.size[1] / 10), texts, font=setFont, fill=fillColor)
        draw.text((100,image.size[1]-150), texts, font=setFont, fill=fillColor)
       # print(image.size[1]-image.size[1] / 10) print(image.size[0]) print(image.size[0]/10) print(image.size[0])
        image.save(outpath,'jpeg')
    return 0

def baidu_map(x,y ):
    strc = x + "," + y
    paramss = {'location': '', 'ak': 'yourAK', 'output': 'json'}
    paramss['location'] = strc
    r = requests.get(url='http://api.map.baidu.com/geocoder',
                     params=paramss)
    result = r.json()

    print(result)
    city = result['result']['addressComponent']['city']
    qu = result['result']['addressComponent']['district']
    aaab=result['result']['business']
    print(aaab)
    return city + qu+aaab
def geocode(location):
    parameters = {'location': location, 'key': '7ec25a9c6716bb26f0d25e9fdfa012b8'}
    base = 'http://restapi.amap.com/v3/geocode/regeo'
    response = requests.get(base, parameters)
    answer = response.json()


    json_dicts=json.dumps(answer,indent=4,ensure_ascii=False)

    print(json_dicts)
    return answer['regeocode']['addressComponent']['province'], answer['regeocode'][
        'addressComponent']['district']
      #  , answer['regeocode']['addressComponent']['businessAreas'][0]['name']
def calculate_age(born):
    today=datetime.now()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        # raised when birth date is February 29
        # and the current year is not a leap year
        birthday = born.replace(year=today.year, day=born.day - 1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def calculate_pict_age(born,yy):
    #照片的年龄
    today=yy
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        # raised when birth date is February 29
        # and the current year is not a leap year
        birthday = born.replace(year=today.year, day=born.day - 1)
    print(birthday, today)
    if birthday > today:
        return today.year - born.year - 1
        print ("大于")
    else:
        return today.year - born.year

def days(str1,str2):
   date1=datetime.strptime(str1[0:10],"%Y-%m-%d")
   date2=datetime.strptime(str2[0:10],"%Y-%m-%d")
   num=(date1-date2).days
   return num

def months(str1,str2):
    year1=datetime.strptime(str1[0:10],"%Y-%m-%d").year
    year2=datetime.strptime(str2[0:10],"%Y-%m-%d").year
    month1=datetime.strptime(str1[0:10],"%Y-%m-%d").month
    month2=datetime.strptime(str2[0:10],"%Y-%m-%d").month
    num=(year1-year2)*12+(month1-month2)
    return num


if __name__ == '__main__':

    for parent, dirnames, filemanes in os.walk(r'E:\photo\yy'):
        #print(parent, dirnames, filemanes )
        for filemane in filemanes:
            nametype = os.path.join(parent, filemane)
            图片名称="d:\\text\\"+filemane.split('.')[0]+"ss.jpg"

            #print(nametype,图片名称)
            lujing = nametype
            经纬度 = exifread_infos(lujing)  # 获取照片的经纬
           # print(经纬度)
            aa= len(经纬度)
            #print(len(aa))
            #print(type(aa))


            if aa == 3 :

          #   print(len(经纬度)) print(type(经纬度)) print(经纬度)
             #strc = baidu_map(str(经纬度[1]), str(经纬度[2]))
             #print( str(经纬度[2]),str(经纬度[1]))
             strc = geocode(str(经纬度[2])+','+str(经纬度[1]))
             print(strc)

             照片日期 = datetime.strptime(经纬度[0], "%Y:%m:%d %H:%M:%S")
             出生日期 = datetime.strptime('2017:04:27 20:40:21', "%Y:%m:%d %H:%M:%S")
             打印拍照年月日 = str(照片日期.year) + "." + str(照片日期.month) + "." + str(照片日期.day)
             出生天数 = days(str(照片日期), str(出生日期))
             出生月数 = months(str(照片日期), str(出生日期))
             add_num(lujing, 打印拍照年月日 + " " + str(出生天数) + "天 " + str(出生月数) + "月 " + str(strc), 图片名称)

            else:
                print("信息不完整"+filemane)



'''lujing = "e:/photo/li.jpg"
 out="e:/photo/xx.jpg"
 经纬度=exifread_infos(lujing) #获取照片的经纬
 strc=baidu_map(str(经纬度[1]),str(经纬度[2]))
 照片日期=datetime.strptime(经纬度[0], "%Y:%m:%d %H:%M:%S")
 出生日期=datetime.strptime('2016:10:28 20:40:21', "%Y:%m:%d %H:%M:%S")
 打印拍照年月日 = str(照片日期.year)+"." + str(照片日期.month) +"."+ str(照片日期.day)
 出生天数=days(str(照片日期),str(出生日期))
 出生月数=months(str(照片日期),str(出生日期))
 add_num(lujing, 打印拍照年月日 + " "+str(出生天数)+"天 "+str(出生月数)+"月 "+strc,out)
 


 
 lujing = "e:/photo/2.jpg"
 print(exifread_infos(lujing))
 经纬度=exifread_infos(lujing) #获取照片的经纬
 strc=baidu_map(str(经纬度[1]),str(经纬度[2]))
 add_num(lujing,经纬度[0]+strc)
 print("打印时间")
 照片日期=datetime.strptime(经纬度[0], "%Y:%m:%d %H:%M:%S")

 print (照片日期)
 出生日期=datetime.strptime('2016:10:28 20:40:21', "%Y:%m:%d %H:%M:%S")
 #print(出生日期)
 打印拍照年月日 = str(照片日期.year)+"." + str(照片日期.month) +"."+ str(照片日期.day)
 print(打印拍照年月日)
 #print(calculate_age(出生日期))
 print(calculate_pict_age(出生日期,照片日期))
 #print(borntime.tm_year)
 #shijian=datetime.strptime(经伟度[0], "%Y:%m:%d")

 出生天数=days(str(照片日期),str(出生日期))
 出生月数=months(str(照片日期),str(出生日期))
 add_num(lujing, 打印拍照年月日 + " "+str(出生天数)+"天 "+str(出生月数)+"月 "+strc)
 '''


