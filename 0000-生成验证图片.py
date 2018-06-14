from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
# import PIL
# im = Image.open('c:/users/ETA/Desktop/presys_bug/2.jpg')
# print(im)
# print(type(im))
# w,h = im.size
# print('the original size is %d*%d' %(w,h))
# im.thumbnail((w*4, h*4))
# print(im)
def create_image(size, mode='RGB',color=(255,182,255)):
    return Image.new(mode='RGB', size=size,color=color)


# 生成随机验证码字符
def rand_char():
    return chr(random.randint(65,90))


# 生成随机颜色（背景色）
def rand_color1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))


# 生成随机颜色（字符颜色）
def rand_color2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))


if __name__=='__main__':
    width = 240
    height = 60
    # 创建纯色的背景图片
    im = create_image((width,height))
    # 创建字符字体对象
    font = ImageFont.truetype('c:/Windows/Fonts/Arial.ttf', 36)
    # 创建Draw 对象
    draw = ImageDraw.Draw(im)
    #print(draw)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rand_color1())
    #  输出字符
    for p in range(4):
        draw.text((60*p+10,10),text=rand_char(),fill=rand_color2(),font=font)
    # 虚化图片
    im = im.filter(ImageFilter.BoxBlur(2))
    # 保存图片
    im.save('./image/01-test.jpg','jpeg')


# im2.save('c:/users/ETA/Desktop/presys_bug/2-2.png','png')
