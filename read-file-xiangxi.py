import win32api
import requests
from PIL import Image,ImageDraw,ImageFont

def getFileProperties(fname):
      """
      读取给定文件的所有属性, 返回一个字典.
      """
      print ("开始读文件")
      propNames = ('Comments', 'InternalName', 'ProductName',
                 'CompanyName', 'LegalCopyright', 'ProductVersion',
                 'FileDescription', 'LegalTrademarks', 'PrivateBuild',
                 'FileVersion', 'OriginalFilename', 'SpecialBuild')

      props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}
      #try:
      print(fname)
      fixedInfo = win32api.GetFileVersionInfo(fname, '\\')

      print (fname)
      props['FixedFileInfo'] = fixedInfo
      props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                                                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                                                fixedInfo['FileVersionLS'] % 65536)

       # \VarFileInfo\Translation returns list of available (language, codepage)
      # pairs that can be used to retreive string info. We are using only the first pair.
      lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

       # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
      # two are language/codepage pair returned from above

      strInfo = {}
      for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
           # print (strinfo)
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)
            print (propName)
      props['StringFileInfo'] = strInfo
    #except:
        #pass

    #return props

#print  abc=getFileProperties(r'D:\python\xin\abc.xls')
#if __name__ = "__main__":
#aa = getFileProperties("./python37.exe")
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

if __name__ == '__main__':
    lujing = "e:/photo/1.jpg"
    new_lujing = "e:/photo/1.jpg"

    #aa = getFileProperties(lujing)

    print (exifread_infos(lujing))
    #print(aa)
    r = requests.get(url='http://api.map.baidu.com/geocoder',
                     params={'location': '39.90561676, 116.62898254388888', 'ak': 'yourAK', 'output': 'json'})

    result = r.json()
    print(result)
    city = result['result']['addressComponent']['city']
    qu = result['result']['addressComponent']['district']
    print(city+qu)


    im = Image.open(lujing).convert('RGBA')
    txt=Image.new('RGBA', im.size, (0,0,0,0))
    fnt=ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 200)
    d=ImageDraw.Draw(txt)
   # d.text((txt.size[0]-80,txt.size[1]-30),"cnBl6666666666666666666666666666666666ogs",font=fnt,fill=(255,255,255,255))
    #d.text((40, 40),"cnBl6666666666666666666666666666666666ogs", fill=(0, 0, 0), font=fnt)
    d.text((im.size[0] / 2, im.size[1] / 2),'杨利伟', fill='black', font=fnt)
    out=Image.alpha_composite(im,txt)
    out.show()
    Image.SAVE(new_lujing)

