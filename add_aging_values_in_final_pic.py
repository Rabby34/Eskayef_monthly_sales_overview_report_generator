import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys

def crore(number):
    number = number / 10000000
    number = round(number,1)
    number = format(number, ',')
    number = number + ' Cr'
    return number

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

top6_customer_df = pd.read_sql_query("""
select  CASE
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=30 THEN '30 Days'
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>30 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=45 THEN '45 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>45 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=60 THEN '60 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>60 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=90 THEN '90 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>90 THEN '90+ Days'
    ELSE 'Over 90'
END 

as aging,sum(OUT_NET) as outstanding
from cust_out
group by 
 CASE
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=30 THEN '30 Days'
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>30 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=45 THEN '45 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>45 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=60 THEN '60 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>60 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=90 THEN '90 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>90 THEN '90+ Days'
    ELSE 'Over 90'
END 
order by aging ASC""", connection)

customer_name = top6_customer_df['aging'].values.tolist()
bought_values = top6_customer_df['outstanding'].values.tolist()

img = Image.open("final_chemist_pic_with_value.png")
top_customer1_sale = ImageDraw.Draw(img)
top_customer2_sale = ImageDraw.Draw(img)
top_customer3_sale = ImageDraw.Draw(img)
top_customer4_sale = ImageDraw.Draw(img)
top_customer5_sale = ImageDraw.Draw(img)
top_customer6_sale = ImageDraw.Draw(img)

top_customer1_name = ImageDraw.Draw(img)
top_customer2_name = ImageDraw.Draw(img)
top_customer3_name = ImageDraw.Draw(img)
top_customer4_name = ImageDraw.Draw(img)
top_customer5_name = ImageDraw.Draw(img)
top_customer6_name = ImageDraw.Draw(img)

below_title5 = ImageDraw.Draw(img)

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")
font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 21, encoding="unic")

top_customer1_name.text((780, 3050), customer_name[0], (207,65,59), font=font5)
top_customer1_name.text((780, 3051), customer_name[0], (207,65,59), font=font5)

top_customer2_name.text((870, 3050), customer_name[1], (207,65,59), font=font5)
top_customer2_name.text((870, 3051), customer_name[1], (207,65,59), font=font5)

top_customer3_name.text((960, 3050), customer_name[2], (207,65,59), font=font5)
top_customer3_name.text((960, 3051), customer_name[2], (207,65,59), font=font5)

top_customer4_name.text((1055, 3050), customer_name[3], (207,65,59), font=font5)
top_customer4_name.text((1055, 3051), customer_name[3], (207,65,59), font=font5)

top_customer5_name.text((1150, 3050), customer_name[4], (207,65,59), font=font5)
top_customer5_name.text((1150, 3051), customer_name[4], (207,65,59), font=font5)


below_title5.text((900, 2720), "Aging Outstanding", (7,24,24), font=font7)
below_title5.text((900, 2721), "Aging Outstanding", (7,24,24), font=font7)
#below_title5.text((150, 11), "Contribution of Top 6 NSM", (7,24,24), font=font7)

below_title5.text((-20,3115), '''       If there is any inconvenience, you are requested to communicate with the ERP BI Service:\n       (Mobile: 01713-389972, 01713-380499)'''
         ,(164,78,24), font=font6)

img.save('final_output_with_aging.png')

print('aging with values generated')