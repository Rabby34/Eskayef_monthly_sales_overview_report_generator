from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime

date = datetime.today()
day = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
tz_NY = pytz.timezone('Asia/Dhaka')
datetime_BD = datetime.now(tz_NY)
time = datetime_BD.strftime("%I:%M %p")
date = datetime.today()
x = dd.datetime.now()
day = str(date.day) + '-' + str(x.strftime("%b")) + '-' + str(date.year)
print(date)
print(day)
tz_NY = pytz.timezone('Asia/Dhaka')
datetime_BD = datetime.now(tz_NY)
time = datetime_BD.strftime("%I:%M %p")
print(datetime_BD)
print(time)
img = Image.open("banner.png")
title = ImageDraw.Draw(img)
timestore = ImageDraw.Draw(img)
tag = ImageDraw.Draw(img)
branch = ImageDraw.Draw(img)
font = ImageFont.truetype("Stencil_Regular.ttf", 17, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 17, encoding="unic")
font2 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 17, encoding="unic")


# timestore.text((32, 135), time + "\n" + day, (22,76,75), font=font2)
# timestore.text((32+1, 135+1), time + "\n" + day, (22,76,75), font=font2)

timestore.text((1061, 50), day, (255,255,255), font=font2)
timestore.text((1061+1, 50+1), day, (255,255,255), font=font2)

timestore.text((1075, 100), time, (255,255,255), font=font2)
timestore.text((1075+1, 100+1), time, (255,255,255), font=font2)

img.save('tcpl_banner.png')

print('Cover pic with date generated')