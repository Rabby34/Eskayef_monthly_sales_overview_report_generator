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

top6_customer_df = pd.read_sql_query("""declare @date varchar (6) = CONVERT(varchar(8), dateAdd(day,0,getdate()), 112) 
select NSMNAME,EMPSHORTNAME, SUM(EXTINVMISC) as sales from 
(select MSOTR, extinvmisc from OESALESDETAILS
where LEFT(TRANSDATE,6)=@date) as sales
left join(
select distinct msotr,NSMID,NSMNAME from rfieldforce
where yearmonth=@date) as nsm
on sales.msotr=nsm.MSOTR
left join(
select EMPID,EMPSHORTNAME from RFieldForce_SHORT
) as short
on short.EMPID=nsm.NSMID
where short.EMPSHORTNAME is not null
group by NSMNAME,EMPSHORTNAME
order by sales desc""", connection)

customer_name = top6_customer_df['EMPSHORTNAME'].values.tolist()
bought_values = top6_customer_df['sales'].values.tolist()
print(bought_values)

total_amount=sum(bought_values)
print(total_amount)
percent_array=[]

for x in bought_values:
    percen=(x/total_amount)*100;
    percent_array.append(percen)
print(percent_array)


img = Image.open("top_9_nsm_v2.png")
top_customer1_sale = ImageDraw.Draw(img)
top_customer2_sale = ImageDraw.Draw(img)
top_customer3_sale = ImageDraw.Draw(img)
top_customer4_sale = ImageDraw.Draw(img)
top_customer5_sale = ImageDraw.Draw(img)
top_customer6_sale = ImageDraw.Draw(img)
top_customer7_sale = ImageDraw.Draw(img)
top_customer8_sale = ImageDraw.Draw(img)
top_customer9_sale = ImageDraw.Draw(img)

top_customer1_percentage = ImageDraw.Draw(img)
top_customer2_percentage = ImageDraw.Draw(img)
top_customer3_percentage = ImageDraw.Draw(img)
top_customer4_percentage = ImageDraw.Draw(img)
top_customer5_percentage = ImageDraw.Draw(img)
top_customer6_percentage = ImageDraw.Draw(img)
top_customer7_percentage = ImageDraw.Draw(img)
top_customer8_percentage = ImageDraw.Draw(img)
top_customer9_percentage = ImageDraw.Draw(img)

top_customer1_name = ImageDraw.Draw(img)
top_customer2_name = ImageDraw.Draw(img)
top_customer3_name = ImageDraw.Draw(img)
top_customer4_name = ImageDraw.Draw(img)
top_customer5_name = ImageDraw.Draw(img)
top_customer6_name = ImageDraw.Draw(img)
top_customer7_name = ImageDraw.Draw(img)
top_customer8_name = ImageDraw.Draw(img)
top_customer9_name = ImageDraw.Draw(img)

below_title5 = ImageDraw.Draw(img)

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")
font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 14, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 21, encoding="unic")


top_customer1_sale.text((38, 270), crore(bought_values[0]), (34,40,40), font=font5)
top_customer1_sale.text((38, 271), crore(bought_values[0]), (34,40,40), font=font5)

top_customer2_sale.text((168, 270), crore(bought_values[1]), (34,40,40), font=font5)#23 15
top_customer2_sale.text((168, 271), crore(bought_values[1]), (34,40,40), font=font5)

top_customer3_sale.text((310, 270), crore(bought_values[2]), (34,40,40), font=font5)
top_customer3_sale.text((310, 271), crore(bought_values[2]), (34,40,40), font=font5)
#
top_customer4_sale.text((455, 270), crore(bought_values[3]), (34,40,40), font=font5)
top_customer4_sale.text((455, 271), crore(bought_values[3]), (34,40,40), font=font5)
#
top_customer5_sale.text((590, 270), crore(bought_values[4]), (34,40,40), font=font5)
top_customer5_sale.text((590, 271), crore(bought_values[4]), (34,40,40), font=font5)
#
top_customer6_sale.text((737, 270), crore(bought_values[5]), (34,40,40), font=font5)
top_customer6_sale.text((737, 271), crore(bought_values[5]), (34,40,40), font=font5)

top_customer6_sale.text((882, 270), crore(bought_values[6]), (34,40,40), font=font5)
top_customer6_sale.text((882, 271), crore(bought_values[6]), (34,40,40), font=font5)

top_customer6_sale.text((1025, 270), crore(bought_values[7]), (34,40,40), font=font5)
top_customer6_sale.text((1025, 271), crore(bought_values[7]), (34,40,40), font=font5)

top_customer6_sale.text((1170, 270), crore(bought_values[8]), (34,40,40), font=font5)
top_customer6_sale.text((1170, 271), crore(bought_values[8]), (34,40,40), font=font5)

#--------------------------------------------------------------------------------------

top_customer1_name.text((40, 250), customer_name[0], (238, 57, 102), font=font5)
top_customer1_name.text((40, 251), customer_name[0], (238, 57, 102), font=font5)

top_customer2_name.text((172, 250), customer_name[1], (119, 72, 196), font=font5)
top_customer2_name.text((172, 251), customer_name[1], (119, 72, 196), font=font5)

top_customer3_name.text((305, 250), customer_name[2], (3,145,155), font=font5)
top_customer3_name.text((305, 251), customer_name[2], (3,145,155), font=font5)
#
top_customer4_name.text((455, 250), customer_name[3], (231,115,6), font=font5)
top_customer4_name.text((455, 251), customer_name[3], (231,115,6), font=font5)
#
top_customer5_name.text((585, 250), customer_name[4], (21,132,93), font=font5)
top_customer5_name.text((585, 251), customer_name[4], (21,132,93), font=font5)
#
top_customer6_name.text((727, 250), customer_name[5], (222,153,17), font=font5)
top_customer6_name.text((727, 251), customer_name[5], (222,153,17), font=font5)

top_customer7_name.text((882, 250), customer_name[6], (27,166,209), font=font5)
top_customer6_name.text((882, 251), customer_name[6], (27,166,209), font=font5)

top_customer8_name.text((1010, 250), customer_name[7], (176,98,29), font=font5)
top_customer6_name.text((1010, 251), customer_name[7], (176,98,29), font=font5)

top_customer9_name.text((1165, 250), customer_name[8], (82,180,70), font=font5)
top_customer6_name.text((1165, 251), customer_name[8], (82,180,70), font=font5)

#-------------------------------------------------------------------------------

top_customer1_percentage.text((42, 290), '('+str(int(percent_array[0]))+'%)', (22,30,150), font=font6)
top_customer1_percentage.text((42, 291), '('+str(int(percent_array[0]))+'%)', (22,30,150), font=font6)

top_customer2_percentage.text((174, 290), '('+str(int(percent_array[1]))+'%)', (22,30,150), font=font6)#23 15
top_customer2_percentage.text((174, 291), '('+str(int(percent_array[1]))+'%)', (22,30,150), font=font6)

top_customer3_percentage.text((313, 290), '('+str(int(percent_array[2]))+'%)', (22,30,150), font=font6)
top_customer3_percentage.text((313, 291), '('+str(int(percent_array[2]))+'%)', (22,30,150), font=font6)
#
top_customer4_percentage.text((460, 290), '('+str(int(percent_array[3]))+'%)', (22,30,150), font=font6)
top_customer4_percentage.text((460, 291), '('+str(int(percent_array[3]))+'%)', (22,30,150), font=font6)
#
top_customer5_percentage.text((595, 290), '('+str(int(percent_array[4]))+'%)', (22,30,150), font=font6)
top_customer5_percentage.text((595, 291), '('+str(int(percent_array[4]))+'%)', (22,30,150), font=font6)
#
top_customer6_percentage.text((742, 290), '('+str(int(percent_array[5]))+'%)', (22,30,150), font=font6)
top_customer6_percentage.text((742, 291), '('+str(int(percent_array[5]))+'%)', (22,30,150), font=font6)

top_customer7_percentage.text((884, 290), '('+str(int(percent_array[6]))+'%)', (22,30,150), font=font6)
top_customer7_percentage.text((884, 291), '('+str(int(percent_array[6]))+'%)', (22,30,150), font=font6)

top_customer8_percentage.text((1030, 290), '('+str(int(percent_array[7]))+'%)', (22,30,150), font=font6)
top_customer8_percentage.text((1030, 291), '('+str(int(percent_array[7]))+'%)', (22,30,150), font=font6)

top_customer9_percentage.text((1175, 290), '('+str(int(percent_array[8]))+'%)', (22,30,150), font=font6)
top_customer9_percentage.text((1175, 291), '('+str(int(percent_array[8]))+'%)', (22,30,150), font=font6)

below_title5.text((570, 60), "All NSM Contribution", (7,21,21), font=font7)
#below_title5.text((150, 11), "Contribution of Top 6 NSM", (7,24,24), font=font7)

img.save('./top9_customer_info.png')

print('15. Top 6 valuable customer with values generated')