import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
import numpy as np
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
ever_sale_df = pd.read_sql_query("""select right(formatdate,2) as days,isnull(amount,0) as Amount from (
select formatdate from [Calendar] where left(formatdate,6)=convert(varchar(6), GETDATE(),112)) as cal
left join (
select cast(transdate as varchar(8)) as Transdate,sum(EXTINVMISC)/10000000 as amount from OESalesdetails
where left(transdate,6)=convert(varchar(6), GETDATE(),112)
and TRANSTYPE=1 
group by cast(transdate as varchar(8))) as sales
on cal.formatdate=sales.Transdate
order by formatdate""", connection)

all_days_in_month=ever_sale_df['days'].tolist()
day_to_day_sale = ever_sale_df['Amount'].tolist()
# print(all_days_in_month)
# print(day_to_day_sale)

from datetime import date

today = date.today()

current_day = today.strftime("%d")
current_day_in_int=int(current_day)
# print(current_day_in_int)

# sys.exit()
final_days_array=[]
final_sales_array=[]
for t_va in range(0, current_day_in_int):
    #print(t_va)
    final_days_array.append(all_days_in_month[t_va])
    final_sales_array.append(day_to_day_sale[t_va])

# print(final_days_array)
# print(final_sales_array)

EveryD_Target2_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
                Declare @DaysInMonth NVARCHAR(MAX);
                SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                SET @DaysInMonth = DAY(EOMONTH(GETDATE())) 
                select ISNULL(((Sum(TARGET)/@DaysInMonth)/10000000), 0) as  YesterdayTarget from TDCL_BranchTarget  
                where YEARMONTH = @CurrentMonth""", connection)
totarget = EveryD_Target2_df.values
target_for_target = totarget[0, 0]
# print(target_for_target)

y_pos = np.arange(len(final_days_array))

n = 1
Target_to_plot = []
labell_to_plot = []
for z in y_pos:
    labell_to_plot.append(n)
    Target_to_plot.append(int(target_for_target / 1000))
    n = n + 1

# print(Target_to_plot)
# print(labell_to_plot)
#labell.append(20)

#sys.exit()
# ----------------code for cumulitive sales------------
import calendar
import datetime

now = datetime.datetime.now()
total_days = calendar.monthrange(now.year, now.month)[1]
# print(total_days)

new_target = target_for_target
labell_to_plot
z = len(labell_to_plot)
# print(len(labell))
fin_target = 0
cumulative_target_that_needs_to_plot = []
for t_value in range(0, total_days + 1):
    # print(t_value)
    fin_target = new_target * t_value
    # print(fin_target)
    cumulative_target_that_needs_to_plot.append(fin_target)
    fin_target = 0
#print(ttt) #-------------------target data

values = final_sales_array
length = len(values)

new_array = [0]
final = 0
for val in values:
    # print(val)
    get_in = values.index(val)
    # print(get_in)
    if get_in == 0:
        new_array.append(val)
    else:
        for i in range(0, get_in + 1):
            final = final + values[i]
        new_array.append(final)
        final = 0

# print(every_day_sale)
# print(new_array)#--------------------------sales data

x = range(len(cumulative_target_that_needs_to_plot))
xx = range(len(new_array))

list_index_for_target = len(cumulative_target_that_needs_to_plot) - 1
# print(list_index_for_target)

list_index_for_sale = len(new_array) - 1


img = Image.open("Cumulative_Day_Wise_Target_vs_Sales.png")

brand1_name = ImageDraw.Draw(img)
#22,68
w, h = 210, 80
shape1 = [(55, 10), (w , h )]
w1, h1 = 365, 80
shape2 = [(210, 10), (w1 , h1 )]
w2, h2 = 520, 80
shape3 = [(365, 10), (w2 , h2 )]
w3, h3 = 675, 80
shape4 = [(520, 10), (w3 , h3 )]


# create rectangle image
img1 = ImageDraw.Draw(img)
img1.rectangle(shape1, fill="#e6cdff", outline="black")
img1.rectangle(shape2, fill="#FFA254", outline="black")
img1.rectangle(shape3, fill="#ffcca1", outline="black")
img1.rectangle(shape4, fill="#FDA3B5", outline="black")

font = ImageFont.truetype("Stencil_Regular.ttf", 10, encoding="unic")
font1 = ImageFont.truetype("ROCK.ttf", 17, encoding="unic")
font2 = ImageFont.truetype("ROCK.ttf", 34, encoding="unic")
font4 = ImageFont.truetype("Bitstream_Vera_Sans_Roman.ttf", 12, encoding="unic")
font5 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")
font6 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 14, encoding="unic")
font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 16, encoding="unic")

brand1_name.text((70, 10), format(round(cumulative_target_that_needs_to_plot[list_index_for_target],1),',')+' Cr', (0,0,0), font=font2)
brand1_name.text((70, 11), format(round(cumulative_target_that_needs_to_plot[list_index_for_target],1),',')+' Cr', (0,0,0), font=font2)
brand1_name.text((70, 48), 'Monthly Target', (24,23,136), font=font1)
brand1_name.text((70, 48), 'Monthly Target', (24,23,136), font=font1)
#brand1_name.text((40, 26), 'Monthly Target: '+format(round(cumulative_target_that_needs_to_plot[list_index_for_target],1),',') + ' Cr', (0,0,0), font=font5)
#
brand1_name.text((225, 10), format(round(cumulative_target_that_needs_to_plot[list_index_for_sale],1),',') + ' Cr', (0,0,0), font=font2)
brand1_name.text((225, 11), format(round(cumulative_target_that_needs_to_plot[list_index_for_sale],1),',') + ' Cr', (0,0,0), font=font2)
brand1_name.text((235, 48), 'MTD Target', (24,23,136), font=font1)
brand1_name.text((235, 48), 'MTD Target', (24,23,136), font=font1)
# # brand1_name.text((40, 45),'MTD Target: '+format(round(cumulative_target_that_needs_to_plot[list_index_for_sale],1),',') + ' Cr', (0,0,0), font=font5)
# # brand1_name.text((40, 46),'MTD Target: '+format(round(cumulative_target_that_needs_to_plot[list_index_for_sale],1),',') + ' Cr', (0,0,0), font=font5)
# #
brand1_name.text((382, 10), format(round(new_array[list_index_for_sale],1),',')+ ' Cr', (0,0,0), font=font2)
brand1_name.text((382, 11), format(round(new_array[list_index_for_sale],1),',')+ ' Cr', (0,0,0), font=font2)
brand1_name.text((401, 48), 'MTD Sales', (24,23,136), font=font1)
brand1_name.text((401, 48), 'MTD Sales', (24,23,136), font=font1)
# # brand1_name.text((40, 65), 'MTD Sales: '+format(round(new_array[list_index_for_sale],1),',')+ 'Cr', (0,0,0), font=font5)
# # brand1_name.text((40, 66), 'MTD Sales: '+format(round(new_array[list_index_for_sale],1),',')+ ' Cr', (0,0,0), font=font5)
brand1_name.text((547, 10), format(round(cumulative_target_that_needs_to_plot[list_index_for_sale]-new_array[list_index_for_sale],1),',')+ ' Cr', (0,0,0), font=font2)
brand1_name.text((547, 11), format(round(cumulative_target_that_needs_to_plot[list_index_for_sale]-new_array[list_index_for_sale],1),',')+ ' Cr', (0,0,0), font=font2)
brand1_name.text((552, 48), 'Difference', (24,23,136), font=font1)
brand1_name.text((552, 48), 'Difference', (24,23,136), font=font1)

img.save('cumulative_with_value.png')
print('Cumulative with value')