from wxpy import *
from pyecharts import Map

#因为获取的列表城市都没有带市字，而pyecharts需要带个市字
b = '市'
def s(x):
    return x+b

#因为我好友里面除了广东的外和其他的，剩下非广东的寥寥无几，所以只提取广东的
bot = Bot(cache_path = True)
#friends = bot.friends(update=False).search(province = '北京市')
friends = bot.friends(update=False).search(province = '北京')
#print([x.city for x in friends])
citys = []
for f in friends :
    city = f.city
    print(f)
    citys.append(city)
    print(city)
r = map(s,citys)
cityss = list(r)

#为城市计数
a = {}
for i in cityss:
    a[i] = cityss.count(i)


#print(a)
#a.pop('市')

#把字典进行有序拆分为2个列表
attrs = []
values = []
for value, attr in a.items():
    values.append(attr)
    attrs.append(value)
#开始绘图
map = Map("广东地图示例", width=1200, height=600)
map.add("", attrs, values, maptype='北京', is_visualmap=True, visual_text_color='#000')
map.render("city.html")