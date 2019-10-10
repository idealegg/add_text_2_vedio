#-*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import sys


size=40
out='out.png'
ttf=r'C:\Windows\Fonts\arialbd.ttf'
#print sys.argv
text = sys.argv[1]
fillColor = "#0000ff" 
if len(sys.argv) > 2:
  out=sys.argv[2]
if len(sys.argv) > 3:
  size=int(sys.argv[3])
if len(sys.argv) > 4:
  ttf=sys.argv[4]
setFont = ImageFont.truetype(ttf, size)
#生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
image = Image.new(mode='RGBA', size=(size*len(text), size), color=(255, 255, 255, 0))
# ImageDraw.Draw 简单平面绘图
draw = ImageDraw.Draw(im=image)
draw.text((0,0),text,font=setFont,fill=(0,0,0xff),direction=None)
image.save(out)