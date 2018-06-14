from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

def add_num(im):
    # 作用：给微信或QQ头像添加数字
    # 参数：img - Image对象
    num = str(random.randint(1,10))
    font = ImageFont.truetype('c:/Windows/Fonts/ARLRDBD.TTF', 20)
    draw = ImageDraw.Draw(im)
    width, height = im.size
    draw.text((width-20,-2),num,fill=(255,0,0),font=font)
    im.save('./image/touxiang_new.jpg','jpeg')


if __name__=='__main__':
    im = Image.open('./image/touxiang.jpg')
    add_num(im)
