#-*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

def gen_img(filepath, size=None):
    if size is None:
        size = 400
        #生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
    image = Image.new(mode='RGBA', size=(400, 400), color=(255, 55, 55))
    # ImageDraw.Draw 简单平面绘图
    draw_table = ImageDraw.Draw(im=image)
    # 直接显示图片
    image.show()
    image.save(filepath)

def pic_open(filepath):
    #图片打开与显示
    image = Image.open(filepath)
    return image
        
def get_size(image):
    #获取图像的宽和高
    width, height = image.size
    return width,heitht

def pic_text(filepath,size,text,setFont,fillColor,filename,direction=None):
    print(filepath,size,text,setFont,fillColor)
    #打开图片
    image=pic_open(filepath)
    #新建绘图对象
    draw = ImageDraw.Draw(image)
    #显示图片
    image.show()
    draw.text((40,40),text,font=setFont,fill=fillColor,direction=None)
    image.show()
    #保存
    pic_save(image,filename)
    
def pic_save(image,filename):
    #保存
    image.save(filename)    
        

if __name__=="__main__":

    size=None
    
        
    #** ImageFont模块**
    #选择文字字体和大小
    setFont = ImageFont.truetype('ROCKEB.TTF', 20)
    #设置文字颜色
    fillColor = "#0000ff"   #蓝色
    text="abcd"
    size=(40,40)
    filepath="red.png"
    filename="redsave.png"

    gen_img(filepath)
    #打开图片
    image=pic_open(filepath)
    #添加文字
    pic_text(filepath,size,text,setFont,fillColor,filename,direction=None)
    
    
#ffmpeg -i 仓库实景.mp4 -vf "movie=wenzi.png[watermark];[in][watermark] overlay=main_w-overlay_w-10:main_h-overlay_h-10[out] " output.mp4
#右下角
#ffmpeg -i input.mp4 -i logo.png -filter_complex 'overlay=main_w-overlay_w-10:main_h-overlay_h-10' output.mp4  
#左下角
#ffmpeg -i input.mp4 -i logo.png -filter_complex 'overlay=x=10:y=main_h-overlay_h-10' output.mp4
