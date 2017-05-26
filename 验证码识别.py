# 其实这段代码完全看不懂
# source：https://www.shiyanlou.com/courses/364/labs/1165/document

from PIL import Image
# 一个图像处理lib

import hashlib
'''
Python的hashlib提供了常见的摘要算法
它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
（通常用16进制的字符串表示）
'''

import time
import os
import math

# 实现一个向量空间“向量比较”
class VectorCompare:
    # concordance：一致性
    # magnitude：量级
    def magnitude(self,concordance):
        total = 0
        # iteritems()：迭代输出字典的键值对
        for word,count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)

    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


# 该方法用于将图片转换为矢量
def buildvector(im):
    d1 = {}

    count = 0
    # getdata()：用一行序列返回一幅图像的像素信息
    for i in im.getdata():
        d1[count] = i
        count += 1

    return d1

# 实现一个对象
v = VectorCompare()

# 这是一个训练集
iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 加载训练集
imageset = []


for letter in iconset:
    '''
    os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
    只支持在 Unix, Windows 下使用。
    '''
    for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store": # windows check...
            temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
        imageset.append({letter:temp})


# 打开需要识别的图像并进行处理
im = Image.open("captcha.gif")
im2 = Image.new("P",im.size,255)
im.convert("P")
temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix == 220 or pix == 227: 
            im2.putpixel((y,x),0)



inletter = False
foundletter=False
start = 0
end = 0

letters = []

# 将一张验证码图片切割为一个个的字符
for y in range(im2.size[0]): 
    for x in range(im2.size[1]): 
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))


    inletter=False

count = 0
for letter in letters:
    # hashlib.md5()  生成一个md5的hash对象
    '''
    Hash 就是把任意长度的输入,通过散列算法，变换成固定长度的输出，
    该输出就是散列值,而MD5可以说是目前应用最广泛的Hash算法
    '''
    m = hashlib.md5()
    '''
    crop函数带的参数为(起始点的横坐标，起始点的纵坐标，宽度，高度）
    paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标）
    '''
    # crop()方法：拷贝指定位置的图片
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))

    guess = []

    #将切割得到的验证码小片段与每个训练片段进行比较
    for image in imageset:
        for x,y in image.iteritems():
            if len(y) != 0:
                guess.append( ( v.relation(y[0],buildvector(im3)),x) )

    guess.sort(reverse=True)
    print (),guess[0]

    count += 1