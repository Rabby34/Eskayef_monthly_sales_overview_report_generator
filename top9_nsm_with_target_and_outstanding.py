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

top6_customer_df = pd.read_sql_query("""declare @fromdate varchar(6)=CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)

select NSMNAME,EMPSHORTNAME, SUM(target) as Target, SUM(sales) as Sales, ISNULL(SUM(Outstanding),0) as Outstanding from
(select  NSMID,NSMNAME,rsmtr,sum(Target) as target from RFieldForce
where yearmonth=@fromdate --and nsmname = 'Mr. Golam Haider' --and ccmsotr = 'ccd46'
group by NSMID,NSMNAME, rsmtr) as nsm
left join 
(select case when left(msotr,2) = 'CC' then LEFT(MSOTR,3) else rsmtr end as rsmtr, 
sum(extinvmisc) as sales from OESalesDetails
where LEFT(Transdate,6)=@fromdate
--and case when left(msotr,2) = 'CC' then LEFT(MSOTR,3) else rsmtr end in ('CD', 'CR', 'CS', 'CT', 'DM', 'NM', 'NM')
group by case when left(msotr,2) = 'CC' then LEFT(MSOTR,3) else rsmtr end) as sales
on nsm.rsmtr=sales.rsmtr
left join
(select case when left(msotr,2) = 'CC' then LEFT(MSOTR,3) else rsmtr end as RSMTR, 
SUM(OUT_NET) as Outstanding from ARCOUT.dbo.CUST_OUT where LEFT(INVDATE,6)=@fromdate
group by case when left(msotr,2) = 'CC' then LEFT(MSOTR,3) else rsmtr end) as cout
on sales.rsmtr=cout.rsmtr
left join
(select EMPID,EMPSHORTNAME from RFieldForce_SHORT
) as short
on short.EMPID=nsm.NSMID
where target<>'0'
and short.EMPSHORTNAME is not null
group by NSMNAME,EMPSHORTNAME
order by Sales DESC
""", connection)

customer_name = top6_customer_df['EMPSHORTNAME'].values.tolist()
target_values = top6_customer_df['Target'].values.tolist()
bought_values = top6_customer_df['Sales'].values.tolist()
outstanding = top6_customer_df['Outstanding'].values.tolist()
print(customer_name)
print(target_values)
print(bought_values)
print(outstanding)

# total_amount=sum(bought_values)
# print(total_amount)
# percent_array=[]
#
# for x in bought_values:
#     percen=(x/total_amount)*100;
#     percent_array.append(percen)
# print(percent_array)
# sys.exit()

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



#--------------------------------------------------------------------------------------

top_customer1_name.text((40, 80), customer_name[0], (238, 57, 102), font=font5)
top_customer1_name.text((40, 81), customer_name[0], (238, 57, 102), font=font5)

top_customer2_name.text((172, 80), customer_name[1], (119, 72, 196), font=font5)
top_customer2_name.text((172, 81), customer_name[1], (119, 72, 196), font=font5)

top_customer3_name.text((305, 80), customer_name[2], (3,145,155), font=font5)
top_customer3_name.text((305, 81), customer_name[2], (3,145,155), font=font5)
#
top_customer4_name.text((455, 80), customer_name[3], (231,115,6), font=font5)
top_customer4_name.text((455, 81), customer_name[3], (231,115,6), font=font5)
#
top_customer5_name.text((585, 80), customer_name[4], (21,132,93), font=font5)
top_customer5_name.text((585, 81), customer_name[4], (21,132,93), font=font5)
#
top_customer6_name.text((727, 80), customer_name[5], (222,153,17), font=font5)
top_customer6_name.text((727, 81), customer_name[5], (222,153,17), font=font5)

top_customer7_name.text((882, 80), customer_name[6], (27,166,209), font=font5)
top_customer6_name.text((882, 81), customer_name[6], (27,166,209), font=font5)

top_customer8_name.text((1010, 80), customer_name[7], (176,98,29), font=font5)
top_customer6_name.text((1010, 81), customer_name[7], (176,98,29), font=font5)

top_customer9_name.text((1165, 80), customer_name[8], (82,180,70), font=font5)
top_customer6_name.text((1165, 81), customer_name[8], (82,180,70), font=font5)

#-------------------------------sales------------------------------------------------

top_customer1_name.text((30, 258),'A: '+ crore(bought_values[0]), (0,0,0), font=font5)
top_customer1_name.text((30, 259),'A: '+ crore(bought_values[0]), (0,0,0), font=font5)

top_customer2_name.text((162, 258),'A: '+ crore(bought_values[1]), (0,0,0), font=font5)
top_customer2_name.text((162, 259),'A: '+ crore(bought_values[1]), (0,0,0), font=font5)

top_customer3_name.text((298, 258),'A: '+ crore(bought_values[2]), (0,0,0), font=font5)
top_customer3_name.text((298, 259),'A: '+ crore(bought_values[2]), (0,0,0), font=font5)
#
top_customer4_name.text((445, 258),'A: '+ crore(bought_values[3]), (0,0,0), font=font5)
top_customer4_name.text((445, 259),'A: '+ crore(bought_values[3]), (0,0,0), font=font5)
#
top_customer5_name.text((580, 258),'A: '+ crore(bought_values[4]), (0,0,0), font=font5)
top_customer5_name.text((581, 259),'A: '+ crore(bought_values[4]), (0,0,0), font=font5)

top_customer6_name.text((722, 258),'A: '+ crore(bought_values[5]), (0,0,0), font=font5)
top_customer6_name.text((723, 259),'A: '+ crore(bought_values[5]), (0,0,0), font=font5)

top_customer7_name.text((868, 258),'A: '+ crore(bought_values[6]), (0,0,0), font=font5)
top_customer6_name.text((867, 259),'A: '+ crore(bought_values[6]), (0,0,0), font=font5)

top_customer8_name.text((1015, 258),'A: '+ crore(bought_values[7]), (0,0,0), font=font5)
top_customer6_name.text((1016, 259),'A: '+ crore(bought_values[7]), (0,0,0), font=font5)

top_customer9_name.text((1160, 258),'A: '+ crore(bought_values[8]), (0,0,0), font=font5)
top_customer6_name.text((1160, 259),'A: '+ crore(bought_values[8]), (0,0,0), font=font5)

#---------------------------------target----------------------------------------------

top_customer1_name.text((30, 238),'T: '+ crore(target_values[0]), (0,0,0), font=font5)
top_customer1_name.text((30, 239),'T: '+ crore(target_values[0]), (0,0,0), font=font5)

top_customer2_name.text((162, 238), 'T: '+ crore(target_values[1]), (0,0,0), font=font5)
top_customer2_name.text((162, 239), 'T: '+ crore(target_values[1]), (0,0,0), font=font5)

top_customer3_name.text((298, 238), 'T: '+ crore(target_values[2]), (0,0,0), font=font5)
top_customer3_name.text((298, 239), 'T: '+ crore(target_values[2]), (0,0,0), font=font5)
#
top_customer4_name.text((445, 238), 'T: '+ crore(target_values[3]), (0,0,0), font=font5)
top_customer4_name.text((445, 239), 'T: '+ crore(target_values[3]), (0,0,0), font=font5)
#
top_customer5_name.text((580, 238), 'T: '+ crore(target_values[4]), (0,0,0), font=font5)
top_customer5_name.text((581, 239), 'T: '+ crore(target_values[4]), (0,0,0), font=font5)
#
top_customer6_name.text((722, 238), 'T: '+ crore(target_values[5]), (0,0,0), font=font5)
top_customer6_name.text((723, 239), 'T: '+ crore(target_values[5]), (0,0,0), font=font5)

top_customer7_name.text((868, 238), 'T: '+ crore(target_values[6]), (0,0,0), font=font5)
top_customer6_name.text((867, 239), 'T: '+ crore(target_values[6]), (0,0,0), font=font5)

top_customer8_name.text((1015, 238),'T: '+ crore(target_values[7]), (0,0,0), font=font5)
top_customer6_name.text((1016, 239),'T: '+ crore(target_values[7]), (0,0,0), font=font5)

top_customer9_name.text((1160, 238),'T: '+ crore(target_values[8]), (0,0,0), font=font5)
top_customer6_name.text((1160, 239),'T: '+ crore(target_values[8]), (0,0,0), font=font5)

#---------------------------------------outstanding----------------------------------------

top_customer1_name.text((30, 278),'O: '+ crore(outstanding[0]), (0,0,0), font=font5)
top_customer1_name.text((30, 279),'O: '+ crore(outstanding[0]), (0,0,0), font=font5)

top_customer2_name.text((162, 278), 'O: '+ crore(outstanding[1]), (0,0,0), font=font5)
top_customer2_name.text((162, 279), 'O: '+ crore(outstanding[1]), (0,0,0), font=font5)

top_customer3_name.text((298, 278), 'O: '+ crore(outstanding[2]), (0,0,0), font=font5)
top_customer3_name.text((298, 279), 'O: '+ crore(outstanding[2]), (0,0,0), font=font5)
#
top_customer4_name.text((445, 278), 'O: '+ crore(outstanding[3]), (0,0,0), font=font5)
top_customer4_name.text((445, 279), 'O: '+ crore(outstanding[3]), (0,0,0), font=font5)
#
top_customer5_name.text((580, 278), 'O: '+ crore(outstanding[4]), (0,0,0), font=font5)
top_customer5_name.text((581, 279), 'O: '+ crore(outstanding[4]), (0,0,0), font=font5)
#
top_customer6_name.text((722, 278), 'O: '+ crore(outstanding[5]), (0,0,0), font=font5)
top_customer6_name.text((723, 279), 'O: '+ crore(outstanding[5]), (0,0,0), font=font5)

top_customer7_name.text((868, 278), 'O: '+ crore(outstanding[6]), (0,0,0), font=font5)
top_customer6_name.text((867, 279), 'O: '+ crore(outstanding[6]), (0,0,0), font=font5)

top_customer8_name.text((1015, 278),'O: '+ crore(outstanding[7]), (0,0,0), font=font5)
top_customer6_name.text((1016, 279),'O: '+ crore(outstanding[7]), (0,0,0), font=font5)

top_customer9_name.text((1160, 278),'O: '+ crore(outstanding[8]), (0,0,0), font=font5)
top_customer6_name.text((1160, 279),'O: '+ crore(outstanding[8]), (0,0,0), font=font5)

#---------------------------------achievement----------------------------------------------

top_customer1_name.text((30, 298),'Ac: '+ str(round((bought_values[0]/target_values[0])*100,1))+" %", (0,0,0), font=font5)
top_customer1_name.text((30, 299),'Ac: '+ str(round((bought_values[0]/target_values[0])*100,1))+" %", (0,0,0), font=font5)

top_customer2_name.text((162, 298), 'Ac: '+ str(round((bought_values[1]/target_values[1])*100,1))+" %", (0,0,0), font=font5)
top_customer2_name.text((162, 299), 'Ac: '+ str(round((bought_values[1]/target_values[1])*100,1))+" %", (0,0,0), font=font5)

top_customer3_name.text((298, 298), 'Ac: '+ str(round((bought_values[2]/target_values[2])*100,1))+" %", (0,0,0), font=font5)
top_customer3_name.text((298, 299), 'Ac: '+ str(round((bought_values[2]/target_values[2])*100,1))+" %", (0,0,0), font=font5)
#
top_customer4_name.text((445, 298), 'Ac: '+ str(round((bought_values[3]/target_values[3])*100,1))+" %", (0,0,0), font=font5)
top_customer4_name.text((445, 299), 'Ac: '+ str(round((bought_values[3]/target_values[3])*100,1))+" %", (0,0,0), font=font5)
#
top_customer5_name.text((580, 298), 'Ac: '+ str(round((bought_values[4]/target_values[4])*100,1))+" %", (0,0,0), font=font5)
top_customer5_name.text((581, 299), 'Ac: '+ str(round((bought_values[4]/target_values[4])*100,1))+" %", (0,0,0), font=font5)
#
top_customer6_name.text((722, 298), 'Ac: '+ str(round((bought_values[5]/target_values[5])*100,1))+" %", (0,0,0), font=font5)
top_customer6_name.text((723, 299), 'Ac: '+ str(round((bought_values[5]/target_values[5])*100,1))+" %", (0,0,0), font=font5)

top_customer7_name.text((868, 298), 'Ac: '+ str(round((bought_values[6]/target_values[6])*100,1))+" %", (0,0,0), font=font5)
top_customer6_name.text((867, 299), 'Ac: '+ str(round((bought_values[6]/target_values[6])*100,1))+" %", (0,0,0), font=font5)

top_customer8_name.text((1015, 298),'Ac: '+ str(round((bought_values[7]/target_values[7])*100,1))+" %", (0,0,0), font=font5)
top_customer6_name.text((1016, 299),'Ac: '+ str(round((bought_values[7]/target_values[7])*100,1))+" %", (0,0,0), font=font5)

top_customer9_name.text((1160, 298),'Ac: '+ str(round((bought_values[8]/target_values[8])*100,1))+" %", (0,0,0), font=font5)
top_customer6_name.text((1160, 299),'Ac: '+ str(round((bought_values[8]/target_values[8])*100,1))+" %", (0,0,0), font=font5)


below_title5.text((570, 25), "All NSM Contribution", (7,21,21), font=font7)
#below_title5.text((150, 11), "Contribution of Top 6 NSM", (7,24,24), font=font7)

img.save('./top9_customer_info.png')

print('15. Top 6 valuable customer with values generated')