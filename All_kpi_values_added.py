import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys

def convert(number):
    number = number / 10000000
    number = round(number,1)
    number = format(number, ',')
    number = number + 'Cr'
    return number

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=;'                     # Provide server
                        'DATABASE=;'                   # provide database 
                        'UID=;PWD=')                   # provide username and password

cursor = connection.cursor()

total_target_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
                                      SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                                      select ISNULL((Sum(TARGET)), 0) as  MTDTarget from TDCL_BranchTarget  
                                      where YEARMONTH = @CurrentMonth""", connection)

target = total_target_df['MTDTarget'].values.tolist()

target_value=target[0]

final_target=str(round(target_value/10000000,1))+' Cr'

print("Target value = "+final_target)

total_sales_df = pd.read_sql_query("""select sum(EXTINVMISC) as gross from oesalesdetails
where TRANSTYPE=1
and 
left(transdate,6)=CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)""", connection)

sales = total_sales_df['gross'].values.tolist()

sales_value=sales[0]

final_gross=str(round(sales_value/10000000,1))+" Cr"

print("Gross sales value = ",final_gross)

net_sales_df = pd.read_sql_query("""select sum(EXTINVMISC) as netsales from oesalesdetails
where --TRANSTYPE=1
--and 
left(transdate,6)=CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)""", connection)

net_sales = net_sales_df['netsales'].values.tolist()

net_sales_value = net_sales[0]

final_net=str(round(net_sales_value/10000000,1))+" Cr"

print("net sales value = ",final_net)

achievement=str(round((sales_value/target_value)*100,1))+" %"

print("Achievement percentage = ",achievement)

total_return_percentage_df = pd.read_sql_query("""select ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0)
/ISNULL(sum(case when TRANSTYPE=1 then EXTINVMISC  end), 0)*100 as ReturnPercent 
 from OESalesDetails
where
left(TRANSDATE,6)=convert(varchar(6),getdate(),112)""", connection)

return_percentage = total_return_percentage_df['ReturnPercent'].values.tolist()

final_return_percentage_value=return_percentage[0]

final_return=str(round(return_percentage[0],1))+" %"

print("Return percentage = ",final_return)


from datetime import date, timedelta
from calendar import monthrange

today = date.today()
days_number = today.day
month_number = today.month
year_number = today.year
total_days=monthrange(year_number,month_number)[1]

# print(days_number)
# print(total_days)

trend = (sales_value/days_number)*total_days

final_trend = str(round((trend/10000000),1))+" Cr"
print("Trend = ",final_trend)

trend_achievement = (sales_value/trend)*100

final_trend_achievement=str(round(trend_achievement,1))+" %"
print("Trend Achievement= "+final_trend_achievement)

total_active_customer_df = pd.read_sql_query("""SELECT count(distinct CONCAT(IDCUST, ' ', AUDTORG)) as full_customer
FROM CustomerInformation
where swactv=1""", connection)

active_customer = total_active_customer_df['full_customer'].values.tolist()

customer_ACT=active_customer[0]

ordered_customer_df = pd.read_sql_query("""SELECT count(distinct CONCAT(CUSTOMER, ' ', AUDTORG)) as ordered_customer
FROM OESalesDetails
where LEFT(TRANSDATE,6) = convert(varchar(6), GETDATE(),112)""", connection)

ordered_customer = ordered_customer_df['ordered_customer'].values.tolist()

customer_ORD=ordered_customer[0]

percentage_value = (customer_ORD/customer_ACT)*100

final_cust_cov=str(round(percentage_value,1))+" %"

print("Customer coverage= "+final_cust_cov)


total_active_item_df = pd.read_sql_query("""select count(ITEMNO) as active from PRINFOSKF""", connection)

active_item = total_active_item_df['active'].values.tolist()

item_ACT=active_item[0]

ordered_item_df = pd.read_sql_query("""select count(distinct ITEM) as sold from OESalesDetails""", connection)

ordered_item = ordered_item_df['sold'].values.tolist()

item_ORD=ordered_item[0]

percentage_value_of_item = (item_ORD/item_ACT)*100

final_item_cov=str(round(percentage_value_of_item,1))+" %"

print("Item coverage= "+final_item_cov)




#-----------------------------------------------------------------------------------------

img = Image.open("./final_output_with_aging.png")

brand1_name = ImageDraw.Draw(img)
brand2_name = ImageDraw.Draw(img)
brand3_name = ImageDraw.Draw(img)
brand4_name = ImageDraw.Draw(img)
brand5_name = ImageDraw.Draw(img)
brand6_name = ImageDraw.Draw(img)
brand7_name = ImageDraw.Draw(img)
brand8_name = ImageDraw.Draw(img)
brand9_name = ImageDraw.Draw(img)

box = ImageDraw.Draw(img)

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 11, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 13, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 12, encoding="unic")
font6 = ImageFont.truetype("Century_Gothic_normal.ttf", 55, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 21, encoding="unic")


brand1_name.text((37, 330), final_target, (255,255,255), font=font6)
# brand1_name.text((50, 321), final_target, (255,255,255), font=font6)

brand2_name.text((455, 330), final_gross, (255,255,255), font=font6)
# brand2_name.text((625, 1841), final_gross, (238, 57, 102), font=font6)

brand3_name.text((875, 330), final_net, (255,255,255), font=font6)
# brand3_name.text((625, 1891), final_net, (238, 57, 102), font=font6)

brand4_name.text((37, 510), achievement, (255,255,255), font=font6)
# brand4_name.text((625, 1946), achievement, (238, 57, 102), font=font6)

brand5_name.text((455, 510), final_return, (255,255,255), font=font6)
# brand5_name.text((625, 1996), final_return, (238, 57, 102), font=font6)

brand6_name.text((875, 510), final_trend, (255,255,255), font=font6)
# brand6_name.text((625, 2051), final_trend, (238, 57, 102), font=font6)

brand7_name.text((875, 685), final_trend_achievement,(255,255,255), font=font6)
# brand7_name.text((625, 2101), final_trend_achievement, (238, 57, 102), font=font6)

brand8_name.text((37, 685), final_cust_cov, (255,255,255), font=font6)
# brand8_name.text((625, 2156), final_cust_cov, (238, 57, 102), font=font6)

brand9_name.text((455, 685), final_item_cov, (255,255,255), font=font6)
# brand9_name.text((625, 2206), final_item_cov, (238, 57, 102), font=font6)

# below_title5.text((175, 26), "Top 5 Brand Return", (0,0,0), font=font7)

# box.text((30, 320), '''If there is any inconvenience,\nyou are requested to communicate with the ERP BI Service:\n(Mobile: 01713-389972, 01713-380499)'''
#          ,(164,78,24), font=font5)

img.save('./final_photo_has_to_be_send.png')

print('Final chemist bar with value generated')