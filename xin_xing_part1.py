from PIL import Image
import os
import math
import random

# 所有需处理图片及生成图片的根目录
#dir = "D:\Python3.7.0\one\心型图照片"
dir = "D:\Python3.7.0\one\心型图照片"
# 要处理的图片所在的目录
sourDir = '\model'
# 重设大小后的图片保存的目录
transferDir = r'\1'
# 最终拼接的图片保存的目录
resultDir =r'\2'
# 统一图片的高度
HEIGHT_PER_PIC = 100
# 统一图片的宽度
WIDTH_PER_PIC = 100

# 获取指定路径下的所有图片
def getImagesName(dir):
    allPicPath = []  # 所有图片
    print(dir+"目录")
    for root, dirs, files in os.walk(dir):
        for file in files:
            # 可自行添加图片的类型判断
            if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
                print(dir + file)
                strs='/'
                allPicPath.append(dir +strs+file)
    return allPicPath


# 将图片转化为指定大小
def transferSize(allPicPath):
    for i in range(len(allPicPath)):
        # 打开图片
        im = Image.open(allPicPath[i])
        #print(i)
        # 重新设置图片的大小
        out = im.resize((HEIGHT_PER_PIC, WIDTH_PER_PIC), Image.ANTIALIAS)
        # 将图片保存到固定的位置
        out.save(dir + transferDir + '/' + str(i) + '.jpeg')


def main(dir):
    # 根据目录获取所有图片的路径
    allPicPath = getImagesName(dir + sourDir)

    # 将所有图片转化成统一的大小（长宽均设定为100）
    transferSize(allPicPath)

    # 获取所有转换大小后的图片的路径
    allTransPicPath = getImagesName(dir + transferDir)

    # 打印路径，检查是否正确
    # print(allTransPicPath)

    # 得到用于拼图的图片的数量
    numOfPic = len(allTransPicPath)

    # 因为设计拼接后的图形为正方形，因而对图片数量开算数平方根后向下取整，得到拼接后的正方形每行需要的小图片的数量
    perPicNum = math.floor(math.sqrt(numOfPic))

    # 生成一个固定的大小的image，类似于画布的感觉，用于将所有的图片贴上去，再生成新的图片
    toImage = Image.new('RGBA', (perPicNum * HEIGHT_PER_PIC, perPicNum * WIDTH_PER_PIC))

    # 随机打乱转化大小后的图片的顺序，防止图片多余的情况下每次在后头的图片都无法用于拼接，也可使每次拼接出的图顺序不一样
    random.shuffle(allTransPicPath)

    # 遍历用于拼接的图片，将每张图片拼接到指定位置
    for i in range(numOfPic):
        # 获取用于拼接的图片的image
        fromImage = Image.open(allTransPicPath[i])
        # 计算每个图片的位置，保证顺利拼接
        loc = ((int(i / perPicNum) * HEIGHT_PER_PIC), (i % perPicNum) * WIDTH_PER_PIC)
        # 打印每个图片所在的位置，可以看出分布
        print(loc)
        # 在上述生成的画布image上粘贴图片到指定位置
        toImage.paste(fromImage, loc)
    # 在画布上粘贴所有图片后将画布保存到指定位置
    toImage.save(dir + resultDir + '/result.png')


if __name__ == '__main__':
    main(dir)
