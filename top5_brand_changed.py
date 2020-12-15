import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys

import math

millnames = ['',' K',' M',' B',' T']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

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

top5_brand_df = pd.read_sql_query("""Select top 5 BRAND, sum(Target) as target, sum(Sales) as sales,(sum(Sales)/sum(Target))*100 as achv from 
(select ITEMNO,BRAND from prinfoskf
where status='1'
) as a
left join
(select ITEM,SUM(EXTINVMISC) as Sales from OESalesDetails
where LEFT(TRANSDATE,6)=CONVERT(varchar(6), getdate(), 112)
and TRANSTYPE=1
group by ITEM) as c
on c.ITEM=a.ITEMNO
left join
(select ITEMNO,SUM([VALUE]) as Target from ARCSECONDARY.dbo.RfieldForceProductTRG
where YEARMONTH=CONVERT(varchar(6), getdate(), 112)
group by ITEMNO) as b
on a.ITEMNO=b.ITEMNO
where BRAND is not NULL
and target is not NULL
and sales is not NULL
group by BRAND
order by achv DESC
""", connection)

Brand_name = top5_brand_df['BRAND'].values.tolist()
sale_values = top5_brand_df['sales'].values.tolist()
target_values = top5_brand_df['target'].values.tolist()
achv_values = top5_brand_df['achv'].values.tolist()

img = Image.open("./top5_brand.png")
top_brand1_sale = ImageDraw.Draw(img)
top_brand2_sale = ImageDraw.Draw(img)
top_brand3_sale = ImageDraw.Draw(img)
top_brand4_sale = ImageDraw.Draw(img)
top_brand5_sale = ImageDraw.Draw(img)

top_brand1_name = ImageDraw.Draw(img)
top_brand2_name = ImageDraw.Draw(img)
top_brand3_name = ImageDraw.Draw(img)
top_brand4_name = ImageDraw.Draw(img)
top_brand5_name = ImageDraw.Draw(img)

below_title5 = ImageDraw.Draw(img)

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")
font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 17, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 25, encoding="unic")


#-----------------------------------target-----------------------------------------------------
top_brand1_sale.text((193, 298), str(round(target_values[0]/1000,1))+" K", (0,0,0), font=font5)
# top_brand1_sale.text((78, 291), str(round(target_values[0]/1000,1))+" K", (0,0,0), font=font5)

top_brand2_sale.text((314, 298), str(round(target_values[1]/1000,1))+" K", (0,0,0), font=font5)
# top_brand2_sale.text((234, 291), str(round(target_values[1]/1000,1))+" K", (0,0,0), font=font5)

top_brand3_sale.text((435, 298), str(round(target_values[2]/1000,1))+" K", (0,0,0), font=font5)
# top_brand3_sale.text((388, 291), str(round(target_values[2]/1000,1))+" K", (0,0,0), font=font5)

top_brand4_sale.text((556, 298), str(round(target_values[3]/1000,1))+" K", (0,0,0), font=font5)
# top_brand4_sale.text((539, 291), str(round(target_values[3]/1000,1))+" K", (0,0,0), font=font5)

top_brand5_sale.text((677, 298), str(round(target_values[4]/1000,1))+" K", (0,0,0), font=font5)
# top_brand5_sale.text((694, 291), str(round(target_values[4]/1000,1))+" K", (0,0,0), font=font5)

#-----------------------------------------------sales-----------------------------------------------------------
top_brand1_sale.text((193, 324), str(round(sale_values[0]/1000,1))+" K", (0,0,0), font=font5)
# top_brand1_sale.text((78, 191), str(round(achv_values[0],1))+" K", (0,0,0), font=font5)

top_brand2_sale.text((314, 324),str(round(sale_values[1]/1000,1))+" K", (0,0,0), font=font5)
# top_brand2_sale.text((234, 191), str(round(achv_values[1],1))+" %", (0,0,0), font=font5)

top_brand3_sale.text((435, 324), str(round(sale_values[2]/1000,1))+" K", (0,0,0), font=font5)
# top_brand3_sale.text((388, 191), str(round(achv_values[2],1))+" %", (0,0,0), font=font5)

top_brand4_sale.text((556, 324), str(round(sale_values[3]/1000,1))+" K", (0,0,0), font=font5)
# top_brand4_sale.text((539, 191), str(round(achv_values[3],1))+" %", (0,0,0), font=font5)

top_brand5_sale.text((677, 324), str(round(sale_values[4]/1000,1))+" K", (0,0,0), font=font5)
# top_brand5_sale.text((694, 191), str(round(achv_values[4],1))+" %", (0,0,0), font=font5)
#--------------------------------------------------------------------------------------------------------

top_brand1_sale.text((198, 163), str(round(achv_values[0],1))+" %", (29,40,194), font=font5)
# top_brand1_sale.text((78, 191), str(round(achv_values[0],1))+" %", (0,0,0), font=font5)

top_brand2_sale.text((325, 163), str(round(achv_values[1],1))+" %", (29,40,194), font=font5)
# top_brand2_sale.text((234, 191), str(round(achv_values[1],1))+" %", (0,0,0), font=font5)

top_brand3_sale.text((440, 163), str(round(achv_values[2],1))+" %", (29,40,194), font=font5)
# top_brand3_sale.text((388, 191), str(round(achv_values[2],1))+" %", (0,0,0), font=font5)

top_brand4_sale.text((561, 163), str(round(achv_values[3],1))+" %", (29,40,194), font=font5)
# top_brand4_sale.text((539, 191), str(round(achv_values[3],1))+" %", (0,0,0), font=font5)

top_brand5_sale.text((682, 162), str(round(achv_values[4],1))+" %", (29,40,194), font=font5)
# top_brand5_sale.text((694, 191), str(round(achv_values[4],1))+" %", (0,0,0), font=font5)

top_brand1_name.text((193, 245), Brand_name[0], (0,0,132), font=font6)
top_brand1_name.text((193, 246), Brand_name[0], (0,0,132), font=font6)

top_brand2_name.text((316, 245), Brand_name[1], (0,0,132), font=font6)#289, 235
top_brand2_name.text((316, 246), Brand_name[1], (0,0,132), font=font6)

top_brand3_name.text((440, 245), Brand_name[2], (0,0,132), font=font6)
top_brand3_name.text((440, 246), Brand_name[2], (0,0,132), font=font6)

top_brand4_name.text((564, 245), Brand_name[3], (0,0,132), font=font6)
top_brand4_name.text((564, 246), Brand_name[3], (0,0,132), font=font6)

top_brand5_name.text((673, 245), Brand_name[4], (0,0,132), font=font6)
top_brand5_name.text((673, 246), Brand_name[4], (0,0,132), font=font6)

below_title5.text((280, 20), "Top 5 Brand by Achv.", (7,24,24), font=font7)
#below_title5.text((280, 31), "Top 5 Brand Sales", (7,24,24), font=font7)

img.save('./changed_top5_brand_info.png')

print('10. Top 5 branch sales with values generated')