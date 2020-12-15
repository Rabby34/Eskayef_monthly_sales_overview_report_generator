from PIL import Image, ImageDraw, ImageFont, ImageFilter

l_img = Image.open("left_mirror.png")
w, h = l_img.size
l_img.crop((0, 0, w-20, h-0)).save("left_mirror2.png")

r_img = Image.open("right_mirror.png")
w, h = r_img.size
r_img.crop((20, 0, w-0, h-0)).save("right_mirror2.png")

print('pictures are cut')