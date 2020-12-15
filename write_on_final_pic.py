import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys


#
# def convert(number):
#     number = number / 1000
#     number = int(number)
#     number = format(number, ',')
#     number = number + 'K'
#     return number
#
connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=;'                     # Provide server
                        'DATABASE=;'                   # provide database 
                        'UID=;PWD=')                   # provide username and password
#
# cursor = connection.cursor()
#
# top5_return_brand_df = pd.read_sql_query("""
# Select  top 10 b.NAMECUST,c.NAMECUST_ShortName as shortname,a.ret/1000 as returnamount from
# (Select CUSTOMER,ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0) as ret from OESalesDetails
# group by CUSTOMER) as a
# left join
# (Select IDCUST,NAMECUST from CustomerInformation
# group by IDCUST,NAMECUST) as b
# on b.IDCUST = a.CUSTOMER
# left join
# (select IDCUST,NAMECUST_ShortName from Customer_ShortName
# group by IDCUST,NAMECUST_ShortName) as c
# on b.IDCUST = c.IDCUST
# group by b.NAMECUST,c.NAMECUST_ShortName,a.ret
# having a.ret<>0
# order by a.ret DESC""", connection)
#
# brand_name = top5_return_brand_df['shortname'].values.tolist()
# # print(brand_name)
img = Image.open("marge_all1.png")

brand1_name = ImageDraw.Draw(img)
brand2_name = ImageDraw.Draw(img)
brand3_name = ImageDraw.Draw(img)
brand4_name = ImageDraw.Draw(img)
brand5_name = ImageDraw.Draw(img)
brand6_name = ImageDraw.Draw(img)
brand7_name = ImageDraw.Draw(img)
brand8_name = ImageDraw.Draw(img)
brand9_name = ImageDraw.Draw(img)
brand10_name = ImageDraw.Draw(img)

below_title5 = ImageDraw.Draw(img)

subtitle= ImageDraw.Draw(img)

box = ImageDraw.Draw(img)

# font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
# font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
# font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
# font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
# font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 12, encoding="unic")
# font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 14, encoding="unic")
# font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")
# font6 = ImageFont.truetype("Century_Gothic_normal.ttf", 14, encoding="unic")
# font7 = ImageFont.truetype("Century_Gothic_normal.ttf", 16, encoding="unic")
font6 = ImageFont.truetype("CenturyGothicBold.ttf", 19, encoding="unic")
font7 = ImageFont.truetype("CenturyGothicBold.ttf", 26, encoding="unic")
font8 = ImageFont.truetype("CenturyGothicBold.ttf", 22, encoding="unic")

brand1_name.text((322, 908), 'brand1', (0,0,0), font=font6)
brand1_name.text((322, 909), 'brand1', (0,0,0), font=font6)

brand2_name.text((322, 946), 'brand2', (0,0,0), font=font6)
brand2_name.text((322, 947), 'brand2', (0,0,0), font=font6)

brand3_name.text((322, 984), 'brand3', (0,0,0), font=font6)
brand3_name.text((322, 985), 'brand3', (0,0,0), font=font6)

brand4_name.text((322, 1022), 'brand4', (0,0,0), font=font6)
brand4_name.text((322, 1023), 'brand4', (0,0,0), font=font6)

brand5_name.text((322, 1060), 'brand5', (0,0,0), font=font6)
brand5_name.text((322, 1061), 'brand5', (0,0,0), font=font6)

brand6_name.text((322, 1098), 'brand6', (0,0,0), font=font6)
brand6_name.text((322, 1099), 'brand6', (0,0,0), font=font6)

brand7_name.text((322, 1136), 'brand7', (0,0,0), font=font6)
brand7_name.text((322, 1137), 'brand7', (0,0,0), font=font6)

brand8_name.text((322, 1174), 'brand8', (0,0,0), font=font6)
brand8_name.text((322, 1175), 'brand8', (0,0,0), font=font6)

brand9_name.text((322, 1212), 'brand9', (0,0,0), font=font6)
brand9_name.text((322, 1213), 'brand9', (0,0,0), font=font6)

brand10_name.text((322, 1250), 'brand10', (0,0,0), font=font6)
brand10_name.text((322, 1251), 'brand10', (0,0,0), font=font6)

below_title5.text((172, 788), "Top 10 Item Sales and Return", (0,0,0), font=font7)
# below_title5.text((175, 26), "Top 5 Brand Return", (0,0,0), font=font7)

subtitle.text((162, 848), "Sales", (0,0,0), font=font8)
# subtitle.text((162, 849), "Sales", (0,0,0), font=font8)

subtitle.text((492, 848), "Return", (0,0,0), font=font8)

# box.text((30, 320), '''If there is any inconvenience,\nyou are requested to communicate with the ERP BI Service:\n(Mobile: 01713-389972, 01713-380499)'''
#          ,(164,78,24), font=font5)

img.save('final_merged_pic_with_value.png')

print('Final merged pic with value generated')