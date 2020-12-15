import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys
from PIL import Image, ImageDraw, ImageFont

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

total_sales_df = pd.read_sql_query("""Declare @Currentmonth NVARCHAR(MAX);
SET @Currentmonth = convert(varchar(6), GETDATE(),112);
select Sum(EXTINVMISC) as  MTDSales from OESalesDetails
where LEFT(TRANSDATE,6) = @Currentmonth
and transtype=1""", connection)

active_sales = total_sales_df['MTDSales'].values.tolist()

sales_act=active_sales[0]

print(sales_act)

top_sales_df = pd.read_sql_query("""Select top 5 BRAND, sum(Target) as target, sum(Sales) as sales,(sum(Sales)/sum(Target))*100 as achv from 
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
order by achv DESC""", connection)

top_sale = top_sales_df['sales'].values.tolist()

sales_top=sum(top_sale)

print(sales_top)

data = [sales_top,(sales_act-sales_top)]

percentage_value = round((sales_top/sales_act)*100,1)

# percentage_value = 32.2

print(percentage_value)
if(percentage_value<=5):
    img = Image.open("./medicine_percentage/5_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 10):
    img = Image.open("./medicine_percentage/10_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 15):
    img = Image.open("./medicine_percentage/15_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <=20):
    img = Image.open("./medicine_percentage/20_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 25):
    img = Image.open("./medicine_percentage/25_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 30):
    img = Image.open("./medicine_percentage/30_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 35):
    img = Image.open("./medicine_percentage/35_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 40):
    img = Image.open("./medicine_percentage/40_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 45):
    img = Image.open("./medicine_percentage/45_percent.png")
    print_value = str(percentage_value) + "%"
elif (percentage_value <= 50):
    img = Image.open("./medicine_percentage/50_percent.png")
    print_value = str(percentage_value) + "%"

brand1_name = ImageDraw.Draw(img)

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 12, encoding="unic")
font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 20, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 24, encoding="unic")

brand1_name.text((135, 200), print_value, (238, 57, 102), font=font6)

brand1_name.text((80, 10), "Top 5 Brand", (7,21,21), font=font7)
brand1_name.text((90, 40), "Contribution", (7,21,21), font=font6)

# below_title5.text((175, 26), "Top 5 Brand Return", (0,0,0), font=font7)

# box.text((30, 320), '''If there is any inconvenience,\nyou are requested to communicate with the ERP BI Service:\n(Mobile: 01713-389972, 01713-380499)'''
#          ,(164,78,24), font=font5)

img.save('./contribution_pic.png')


