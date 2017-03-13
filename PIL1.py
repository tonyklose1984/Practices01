#coding:utf-8
# from PIL import Image,ImageFilter,ImageDraw,ImageFont
# #load the image
# im = Image.open("1.jpg")
# #show the image
# im.show()
# #blue the image
# im_blur = im.filter(ImageFilter.BLUR)
# im_blur.show()
# #resize the pic
# size = im.size
# print('the image size is:',size)
# w,h = im.size
# im_thumbnail = im.copy()
# im_thumbnail.thumbnail((w/4,h/4))
# im_thumbnail.save('im_thumbnail.jpg')
# im_thumbnail.show()
# #resize 重设图像大小
# re_size = (800,800)
# im_resize = im.resize(re_size)
# im_resize.save('im_resize.jpg')
# im_resize.show()
# #countour 获取图片轮廓
# im_contour = im.filter(ImageFilter.CONTOUR)
# im_contour.save("im_contour.jpg")
# im_contour.show()

from PIL import Image
from pytesser import *

img = Image.open('1.jpg')
img_grey = img.convert('L')

threshold = 140
table = []
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
img_out = img_grey.point(table,'1')
text = image_to_string(img_grey)
print text















