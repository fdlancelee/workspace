'''
Created on 2016年1月7日

@author: FUDIAN
'''
from PIL import Image,ImageFilter
imadd = 'D:/Python/test/1.jpg'

im = Image.open(imadd)

w,h = im.size

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')

print('Original image size: %sx%s' % (w, h))



