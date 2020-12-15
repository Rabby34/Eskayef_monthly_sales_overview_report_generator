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
declare @yeardate varchar(4)=CONVERT(varchar(4), dateAdd(day,0,getdate()), 112)

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
SUM(OUT_NET) as Outstanding from ARCOUT.dbo.CUST_OUT where LEFT(INVDATE,4)=@yeardate
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

img = Image.open("top_9_nsm_v3.png")

# #------------------------------------------------first row----------------------------------------
# w, h = 143, 265
# shape1 = [(20, 240), (w , h )]
# w1, h1 = 266, 265
# shape2 = [(143, 240), (w1 , h1 )]
# w2, h2 = 389, 265
# shape3 = [(266, 240), (w2 , h2 )]
# w3, h3 = 512, 265
# shape4 = [(389, 240), (w3 , h3 )]
# w4, h4 = 635, 265
# shape5 = [(512, 240), (w4 , h4 )]
# w5, h5 = 758, 265
# shape6 = [(635, 240), (w5 , h5 )]
# w6, h6 = 881, 265
# shape7 = [(758, 240), (w6 , h6 )]
# w7, h7 = 1004, 265
# shape8 = [(881, 240), (w7 , h7 )]
# w8, h8 = 1127, 265
# shape9 = [(1004, 240), (w8 , h8 )]
# w9, h9 = 1250, 265
# shape10 = [(1127, 240), (w9 , h9 )]
#
# #------------------------------------------------second row----------------------------------------
# w10, h10 = 143, 290
# shape11 = [(20, 265), (w10 , h10 )]
# w11, h11 = 266, 290
# shape12 = [(143, 265), (w11 , h11 )]
# w12, h12 = 389, 290
# shape13 = [(266, 265), (w12 , h12 )]
# w13, h13 = 512, 290
# shape14 = [(389, 265), (w13 , h13 )]
# w14, h14 = 635, 290
# shape15 = [(512, 265), (w14 , h14 )]
# w15, h15 = 758, 290
# shape16 = [(635, 265), (w15 , h15 )]
# w16, h16 = 881, 290
# shape17 = [(758, 265), (w16 , h16 )]
# w17, h17 = 1004, 290
# shape18 = [(881, 265), (w17 , h17 )]
# w18, h18 = 1127, 290
# shape19 = [(1004, 265), (w18 , h18 )]
# w19, h19 = 1250, 290
# shape20 = [(1127, 265), (w19 , h19 )]
#
# #------------------------------------------------third row----------------------------------------
# w20, h20 = 143, 315
# shape21 = [(20, 290), (w20 , h20 )]
# w21, h21 = 266, 315
# shape22 = [(143, 290), (w21 , h21 )]
# w22, h22 = 389, 315
# shape23 = [(266, 290), (w22 , h22 )]
# w23, h23 = 512, 315
# shape24 = [(389, 290), (w23 , h23 )]
# w24, h24 = 635, 315
# shape25 = [(512, 290), (w24 , h24 )]
# w25, h25 = 758, 315
# shape26 = [(635, 290), (w25 , h25 )]
# w26, h26 = 881, 315
# shape27 = [(758, 290), (w26 , h26 )]
# w27, h27 = 1004, 315
# shape28 = [(881, 290), (w27 , h27 )]
# w28, h28 = 1127, 315
# shape29 = [(1004, 290), (w28 , h28 )]
# w29, h29 = 1250, 315
# shape30 = [(1127, 290), (w29 , h29 )]
#
# #------------------------------------------------fourth row----------------------------------------
# w30, h30 = 143, 340
# shape31 = [(20, 315), (w30 , h30 )]
# w31, h31 = 266, 340
# shape32 = [(143, 315), (w31 , h31 )]
# w32, h32 = 389, 340
# shape33 = [(266, 315), (w32 , h32 )]
# w33, h33 = 512, 340
# shape34 = [(389, 315), (w33 , h33 )]
# w34, h34 = 635, 340
# shape35 = [(512, 315), (w34 , h34 )]
# w35, h35 = 758, 340
# shape36 = [(635, 315), (w35 , h35 )]
# w36, h36 = 881, 340
# shape37 = [(758, 315), (w36 , h36 )]
# w37, h37 = 1004, 340
# shape38 = [(881, 315), (w37 , h37 )]
# w38, h38 = 1127, 340
# shape39 = [(1004, 315), (w38 , h38 )]
# w39, h39 = 1250, 340
# shape40 = [(1127, 315), (w39 , h39 )]
#
# img1 = ImageDraw.Draw(img)
# img1.rectangle(shape1, fill="#EAEAEA", outline="black")
# img1.rectangle(shape2, fill="#EAEAEA", outline="black")
# img1.rectangle(shape3, fill="#EAEAEA", outline="black")
# img1.rectangle(shape4, fill="#EAEAEA", outline="black")
# img1.rectangle(shape5, fill="#EAEAEA", outline="black")
# img1.rectangle(shape6, fill="#EAEAEA", outline="black")
# img1.rectangle(shape7, fill="#EAEAEA", outline="black")
# img1.rectangle(shape8, fill="#EAEAEA", outline="black")
# img1.rectangle(shape9, fill="#EAEAEA", outline="black")
# img1.rectangle(shape10, fill="#EAEAEA", outline="black")
#
# img1.rectangle(shape11, fill="#EAEAEA", outline="black")
# img1.rectangle(shape12, fill="#EAEAEA", outline="black")
# img1.rectangle(shape13, fill="#EAEAEA", outline="black")
# img1.rectangle(shape14, fill="#EAEAEA", outline="black")
# img1.rectangle(shape15, fill="#EAEAEA", outline="black")
# img1.rectangle(shape16, fill="#EAEAEA", outline="black")
# img1.rectangle(shape17, fill="#EAEAEA", outline="black")
# img1.rectangle(shape18, fill="#EAEAEA", outline="black")
# img1.rectangle(shape19, fill="#EAEAEA", outline="black")
# img1.rectangle(shape20, fill="#EAEAEA", outline="black")
#
# img1.rectangle(shape21, fill="#EAEAEA", outline="black")
# img1.rectangle(shape22, fill="#EAEAEA", outline="black")
# img1.rectangle(shape23, fill="#EAEAEA", outline="black")
# img1.rectangle(shape24, fill="#EAEAEA", outline="black")
# img1.rectangle(shape25, fill="#EAEAEA", outline="black")
# img1.rectangle(shape26, fill="#EAEAEA", outline="black")
# img1.rectangle(shape27, fill="#EAEAEA", outline="black")
# img1.rectangle(shape28, fill="#EAEAEA", outline="black")
# img1.rectangle(shape29, fill="#EAEAEA", outline="black")
# img1.rectangle(shape30, fill="#EAEAEA", outline="black")
#
# img1.rectangle(shape31, fill="#EAEAEA", outline="black")
# img1.rectangle(shape32, fill="#EAEAEA", outline="black")
# img1.rectangle(shape33, fill="#EAEAEA", outline="black")
# img1.rectangle(shape34, fill="#EAEAEA", outline="black")
# img1.rectangle(shape35, fill="#EAEAEA", outline="black")
# img1.rectangle(shape36, fill="#EAEAEA", outline="black")
# img1.rectangle(shape37, fill="#EAEAEA", outline="black")
# img1.rectangle(shape38, fill="#EAEAEA", outline="black")
# img1.rectangle(shape39, fill="#EAEAEA", outline="black")
# img1.rectangle(shape40, fill="#EAEAEA", outline="black")

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

top_customer1_name.text((180, 80), customer_name[0], (238, 57, 102), font=font5)
top_customer1_name.text((180, 81), customer_name[0], (238, 57, 102), font=font5)

top_customer2_name.text((295, 80), customer_name[1], (119, 72, 196), font=font5)
top_customer2_name.text((295, 81), customer_name[1], (119, 72, 196), font=font5)

top_customer3_name.text((410, 80), customer_name[2], (3,145,155), font=font5)
top_customer3_name.text((410, 81), customer_name[2], (3,145,155), font=font5)
#
top_customer4_name.text((540, 80), customer_name[3], (231,115,6), font=font5)
top_customer4_name.text((540, 81), customer_name[3], (231,115,6), font=font5)
#
top_customer5_name.text((650, 80), customer_name[4], (21,132,93), font=font5)
top_customer5_name.text((650, 81), customer_name[4], (21,132,93), font=font5)
#
top_customer6_name.text((785, 80), customer_name[5], (222,153,17), font=font5)
top_customer6_name.text((785, 81), customer_name[5], (222,153,17), font=font5)

top_customer7_name.text((912, 80), customer_name[6], (27,166,209), font=font5)
top_customer6_name.text((912, 81), customer_name[6], (27,166,209), font=font5)

top_customer8_name.text((1025, 80), customer_name[7], (176,98,29), font=font5)
top_customer6_name.text((1025, 81), customer_name[7], (176,98,29), font=font5)

top_customer9_name.text((1160, 80), customer_name[8], (82,180,70), font=font5)
top_customer6_name.text((1160, 81), customer_name[8], (82,180,70), font=font5)


#_____________________________________left titles_______________________________________________

top_customer1_name.text((25, 243),'Target', (0,0,0), font=font5)
top_customer1_name.text((25, 268),'Sales', (0,0,0), font=font5)
top_customer1_name.text((25, 293),'Achv %', (29,40,194), font=font5)
top_customer1_name.text((25, 318),'Outstanding', (0,0,0), font=font5)


#-------------------------------sales------------------------------------------------

top_customer1_name.text((170, 268),crore(bought_values[0]), (0,0,0), font=font5)
# top_customer1_name.text((30, 259),'A: '+ crore(bought_values[0]), (0,0,0), font=font5)

top_customer2_name.text((293, 268),crore(bought_values[1]), (0,0,0), font=font5)
# top_customer2_name.text((162, 259),'A: '+ crore(bought_values[1]), (0,0,0), font=font5)

top_customer3_name.text((416, 268),crore(bought_values[2]), (0,0,0), font=font5)
# top_customer3_name.text((298, 259),'A: '+ crore(bought_values[2]), (0,0,0), font=font5)
#
top_customer4_name.text((539, 268),crore(bought_values[3]), (0,0,0), font=font5)
# top_customer4_name.text((445, 259),'A: '+ crore(bought_values[3]), (0,0,0), font=font5)
#
top_customer5_name.text((662, 268),crore(bought_values[4]), (0,0,0), font=font5)
# top_customer5_name.text((581, 259),'A: '+ crore(bought_values[4]), (0,0,0), font=font5)

top_customer6_name.text((785, 268),crore(bought_values[5]), (0,0,0), font=font5)
# top_customer6_name.text((723, 259),'A: '+ crore(bought_values[5]), (0,0,0), font=font5)

top_customer7_name.text((908, 268),crore(bought_values[6]), (0,0,0), font=font5)
# top_customer6_name.text((867, 259),'A: '+ crore(bought_values[6]), (0,0,0), font=font5)

top_customer8_name.text((1031, 268),crore(bought_values[7]), (0,0,0), font=font5)
# top_customer6_name.text((1016, 259),'A: '+ crore(bought_values[7]), (0,0,0), font=font5)

top_customer9_name.text((1154, 268),crore(bought_values[8]), (0,0,0), font=font5)
# top_customer6_name.text((1160, 259),'A: '+ crore(bought_values[8]), (0,0,0), font=font5)

#---------------------------------target----------------------------------------------

top_customer1_name.text((170, 243),crore(target_values[0]), (0,0,0), font=font5)
# top_customer1_name.text((30, 239),'T: '+ crore(target_values[0]), (0,0,0), font=font5)

top_customer2_name.text((293, 243),crore(target_values[1]), (0,0,0), font=font5)
# top_customer2_name.text((162, 239), 'T: '+ crore(target_values[1]), (0,0,0), font=font5)

top_customer3_name.text((416, 243),crore(target_values[2]), (0,0,0), font=font5)
# top_customer3_name.text((298, 239), 'T: '+ crore(target_values[2]), (0,0,0), font=font5)
#
top_customer4_name.text((539, 243),crore(target_values[3]), (0,0,0), font=font5)
# top_customer4_name.text((445, 239), 'T: '+ crore(target_values[3]), (0,0,0), font=font5)
#
top_customer5_name.text((662, 243),crore(target_values[4]), (0,0,0), font=font5)
# top_customer5_name.text((581, 239), 'T: '+ crore(target_values[4]), (0,0,0), font=font5)
#
top_customer6_name.text((785, 243),crore(target_values[5]), (0,0,0), font=font5)
# top_customer6_name.text((723, 239), 'T: '+ crore(target_values[5]), (0,0,0), font=font5)

top_customer7_name.text((908, 243),crore(target_values[6]), (0,0,0), font=font5)
# top_customer6_name.text((867, 239), 'T: '+ crore(target_values[6]), (0,0,0), font=font5)

top_customer8_name.text((1031, 243),crore(target_values[7]), (0,0,0), font=font5)
# top_customer6_name.text((1016, 239),'T: '+ crore(target_values[7]), (0,0,0), font=font5)

top_customer9_name.text((1154, 243),crore(target_values[8]), (0,0,0), font=font5)
# top_customer6_name.text((1160, 239),'T: '+ crore(target_values[8]), (0,0,0), font=font5)

#---------------------------------------outstanding----------------------------------------

top_customer1_name.text((170, 318),crore(outstanding[0]), (0,0,0), font=font5)
# top_customer1_name.text((30, 279),'O: '+ crore(outstanding[0]), (0,0,0), font=font5)

top_customer2_name.text((293, 318),crore(outstanding[1]), (0,0,0), font=font5)
# top_customer2_name.text((162, 279), 'O: '+ crore(outstanding[1]), (0,0,0), font=font5)

top_customer3_name.text((416, 318),crore(outstanding[2]), (0,0,0), font=font5)
# top_customer3_name.text((298, 279), 'O: '+ crore(outstanding[2]), (0,0,0), font=font5)
#
top_customer4_name.text((539, 318),crore(outstanding[3]), (0,0,0), font=font5)
# top_customer4_name.text((445, 279), 'O: '+ crore(outstanding[3]), (0,0,0), font=font5)
#
top_customer5_name.text((662, 318),crore(outstanding[4]), (0,0,0), font=font5)
# top_customer5_name.text((581, 279), 'O: '+ crore(outstanding[4]), (0,0,0), font=font5)
#
top_customer6_name.text((785, 318),crore(outstanding[5]), (0,0,0), font=font5)
# top_customer6_name.text((723, 279), 'O: '+ crore(outstanding[5]), (0,0,0), font=font5)

top_customer7_name.text((908, 318),crore(outstanding[6]), (0,0,0), font=font5)
# top_customer6_name.text((867, 279), 'O: '+ crore(outstanding[6]), (0,0,0), font=font5)

top_customer8_name.text((1031, 318),crore(outstanding[7]), (0,0,0), font=font5)
# top_customer6_name.text((1016, 279),'O: '+ crore(outstanding[7]), (0,0,0), font=font5)

top_customer9_name.text((1154, 318),crore(outstanding[8]), (0,0,0), font=font5)
# top_customer6_name.text((1160, 279),'O: '+ crore(outstanding[8]), (0,0,0), font=font5)

#---------------------------------achievement----------------------------------------------

top_customer1_name.text((170, 293),str(round((bought_values[0]/target_values[0])*100,1))+" %", (29,40,194), font=font5)
# top_customer1_name.text((30, 299),'Ac: '+ str(round((bought_values[0]/target_values[0])*100,1))+" %", (0,0,0), font=font5)

top_customer2_name.text((293, 293),str(round((bought_values[1]/target_values[1])*100,1))+" %", (29,40,194), font=font5)
# top_customer2_name.text((162, 299), 'Ac: '+ str(round((bought_values[1]/target_values[1])*100,1))+" %", (0,0,0), font=font5)

top_customer3_name.text((416, 293),str(round((bought_values[2]/target_values[2])*100,1))+" %", (29,40,194), font=font5)
# top_customer3_name.text((298, 299), 'Ac: '+ str(round((bought_values[2]/target_values[2])*100,1))+" %", (0,0,0), font=font5)
#
top_customer4_name.text((539, 293),str(round((bought_values[3]/target_values[3])*100,1))+" %", (29,40,194), font=font5)
# top_customer4_name.text((445, 299), 'Ac: '+ str(round((bought_values[3]/target_values[3])*100,1))+" %", (0,0,0), font=font5)
#
top_customer5_name.text((662, 293),str(round((bought_values[4]/target_values[4])*100,1))+" %", (29,40,194), font=font5)
# top_customer5_name.text((581, 299), 'Ac: '+ str(round((bought_values[4]/target_values[4])*100,1))+" %", (0,0,0), font=font5)
#
top_customer6_name.text((785, 293),str(round((bought_values[5]/target_values[5])*100,1))+" %", (29,40,194), font=font5)
# top_customer6_name.text((723, 299), 'Ac: '+ str(round((bought_values[5]/target_values[5])*100,1))+" %", (0,0,0), font=font5)

top_customer7_name.text((908, 293),str(round((bought_values[6]/target_values[6])*100,1))+" %", (29,40,194), font=font5)
# top_customer6_name.text((867, 299), 'Ac: '+ str(round((bought_values[6]/target_values[6])*100,1))+" %", (0,0,0), font=font5)

top_customer8_name.text((1031, 293),str(round((bought_values[7]/target_values[7])*100,1))+" %", (29,40,194), font=font5)
# top_customer6_name.text((1016, 299),'Ac: '+ str(round((bought_values[7]/target_values[7])*100,1))+" %", (0,0,0), font=font5)

top_customer9_name.text((1154, 293),str(round((bought_values[8]/target_values[8])*100,1))+" %", (29,40,194), font=font5)
# top_customer6_name.text((1160, 299),'Ac: '+ str(round((bought_values[8]/target_values[8])*100,1))+" %", (0,0,0), font=font5)


below_title5.text((570, 25), "All NSM Contribution", (7,21,21), font=font7)
#below_title5.text((150, 11), "Contribution of Top 6 NSM", (7,24,24), font=font7)

img.save('./top9_customer_info.png')

print('15. Top 6 valuable customer with values generated')