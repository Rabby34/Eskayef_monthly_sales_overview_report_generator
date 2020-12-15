import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys


def convert(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=;'                     # Provide server
                        'DATABASE=;'                   # provide database 
                        'UID=;PWD=')                   # provide username and password

cursor = connection.cursor()

top5_return_brand_df = pd.read_sql_query("""
select top 10 prinfoskf.BRAND as BRAND,Sum(EXTINVMISC)*(-1) as  MTDSales from OESalesDetails,PRINFOSKF 
	where OESalesDetails.ITEM=PRINFOSKF.itemno and
	LEFT(OESalesDetails.TRANSDATE,6) = left(convert(varchar(6), GETDATE(),112),6) 
	and OESalesDetails.TRANSTYPE<>1
	group by prinfoskf.BRAND
	order by MTDSales DESC""", connection)

brand_name = top5_return_brand_df['BRAND'].values.tolist()
# print(brand_name)
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

box = ImageDraw.Draw(img)

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 12, encoding="unic")
font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 20, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 21, encoding="unic")


brand1_name.text((60, 1785), brand_name[0][0:9], (238, 57, 102), font=font6)
brand1_name.text((60, 1786), brand_name[0][0:9], (238, 57, 102), font=font6)

brand2_name.text((60, 1840), brand_name[1][0:9], (238, 57, 102), font=font6)
brand2_name.text((60, 1841), brand_name[1][0:9], (238, 57, 102), font=font6)

brand3_name.text((60, 1890), brand_name[2][0:9], (238, 57, 102), font=font6)
brand3_name.text((60, 1891), brand_name[2][0:9], (238, 57, 102), font=font6)

brand4_name.text((60, 1945), brand_name[3][0:9], (238, 57, 102), font=font6)
brand4_name.text((60, 1946), brand_name[3][0:9], (238, 57, 102), font=font6)

brand5_name.text((60, 1995), brand_name[4][0:9], (238, 57, 102), font=font6)
brand5_name.text((60, 1996), brand_name[4][0:9], (238, 57, 102), font=font6)

brand6_name.text((60, 2050), brand_name[5][0:9], (238, 57, 102), font=font6)
brand6_name.text((60, 2051), brand_name[5][0:9], (238, 57, 102), font=font6)

brand7_name.text((60, 2100), brand_name[6][0:9], (238, 57, 102), font=font6)
brand7_name.text((60, 2101), brand_name[6][0:9], (238, 57, 102), font=font6)

brand8_name.text((60, 2155), brand_name[7][0:9], (238, 57, 102), font=font6)
brand8_name.text((60, 2156), brand_name[7][0:9], (238, 57, 102), font=font6)

brand9_name.text((60, 2205), brand_name[8][0:9], (238, 57, 102), font=font6)
brand9_name.text((60, 2206), brand_name[8][0:9], (238, 57, 102), font=font6)

brand10_name.text((60, 2260), brand_name[9][0:9], (238, 57, 102), font=font6)
brand10_name.text((60, 2261), brand_name[9][0:9], (238, 57, 102), font=font6)

below_title5.text((200, 1700), "Top 10 Brand Return by Sales", (7,21,21), font=font7)
# below_title5.text((175, 26), "Top 5 Brand Return", (0,0,0), font=font7)

# box.text((30, 320), '''If there is any inconvenience,\nyou are requested to communicate with the ERP BI Service:\n(Mobile: 01713-389972, 01713-380499)'''
#          ,(164,78,24), font=font5)

img.save('final_pic_added_return_info.png')

print('14. Final return bar with value generated')