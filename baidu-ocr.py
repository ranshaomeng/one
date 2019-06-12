from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16044038'
API_KEY = 'dWaEmuTACtepKgAfx3uOylZ3'
SECRET_KEY = 'i2abuScoVn0z2hN30AoAvrmbVAnMnoZA'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
print(client)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('a1.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)




