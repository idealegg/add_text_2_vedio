>>> from PIL import Image, ImageDraw, ImageFont
>>> ttfont = ImageFont.truetype('ROCKEB.TTF',20)
>>> im=Image.pen('123.jpg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'pen'
>>> im=Image.open('123.jpg')
>>> draw=ImageDraw.Draw(im)
>>> draw.text((10,10), u'韩寒', fill=(0,0,0),font=ttfont)
>>> im.show()
>>> draw.text((10,10), "adfasdfasfd", fill=(0,0,0),font=ttfont)
>>> im.show()
>>>