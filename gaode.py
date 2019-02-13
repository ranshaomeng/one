#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
利用高德地图api实现地址和经纬度的转换
'''
import requests
import json
def geocode1(address):
        parameters = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251','poitype':'商务写字楼','radius':'0','extensions': 'all'}
        base = 'http://restapi.amap.com/v3/geocode/regeo'
        response = requests.get(base, parameters)
        answer = response.json()
        print(answer)
        #print(address + "的经纬度：", answer['geocodes'][0]['location'])


def geocode(location):
    parameters = {'location': location, 'key': '7ec25a9c6716bb26f0d25e9fdfa012b8'}
    base = 'http://restapi.amap.com/v3/geocode/regeo'
    response = requests.get(base, parameters)
    answer = response.json()
    print(answer)
    return answer['regeocode']['addressComponent']['district'], answer['regeocode'][
        'formatted_address']
if __name__=='__main__':
        #address = input("请输入地址:")
        address = '116.59582519527777,39.88960266111111'
       # geocode(address)
       # print(geocode(address))
        dicts = {"name": "lucy", "sex": "boy"}

        json_dicts = json.dumps(dicts,indent=4)
        print(json_dicts)