# 图像的打开保存与显示
# 引用链接
	# http://blog.csdn.net/followingturing/article/details/7996495
	# http://justcoding.iteye.com/blog/901605

# 引入module
from PIL import Image # 一定要这样写
import matplotlib.pyplot as plt # 目测是一个绘图module

img = Image.open("sample.png") # 打开图片，创建一个实例（相对路径）
plt.figure("dog")  # 创建一个空白图像
plt.imshow(img) # 将图像填充进去
plt.axis('off') # 关闭坐标系
plt.show() # 显示图像

#  将图片关掉以后才会进入以下代码

img.save('C:/Users/zxc78/Desktop/sample.jpg') # 将图片保存为了JPG格式 （绝对路径）
print(img.size)  #图片的尺寸
print(img.mode) #图片的模式
print(img.format)  #图片的格式

new_img = img.resize((128,128),Image.BILINEAR) # 调整尺寸
rot_img = new_img.rotate(45) # 图像旋转45度
rot_img.save("C:/Users/zxc78/Desktop/rot_sample.jpg")