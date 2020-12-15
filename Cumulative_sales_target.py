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
everyday_return_df = pd.read_sql_query("""select right(formatdate,2) as days,isnull(amount,0) as Amount from (
select formatdate from [Calendar] where left(formatdate,6)=convert(varchar(6), GETDATE(),112)) as cal
left join (
select cast(transdate as varchar(8)) as Transdate,(sum(EXTINVMISC)/10000000)*(-1) as amount from OESalesdetails
where left(transdate,6)=convert(varchar(6), GETDATE(),112)
and TRANSTYPE<>1 
group by cast(transdate as varchar(8))) as sales
on cal.formatdate=sales.Transdate
order by formatdate""", connection)

day_to_day_return = everyday_return_df['Amount'].tolist()

from datetime import date

today = date.today()

current_day = today.strftime("%d")
current_day_in_int=int(current_day)
# print(current_day_in_int)

# sys.exit()
final_days_array=[]
final_sales_array=[]
final_return_array=[]
for t_va in range(0, current_day_in_int):
    #print(t_va)
    final_days_array.append(all_days_in_month[t_va])
    final_sales_array.append(day_to_day_sale[t_va])
    final_return_array.append(day_to_day_return[t_va])

# print(final_days_array)
# print(final_sales_array)
# print(final_return_array)

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

values2 = final_return_array
length2 = len(values2)

new_array_of_return = [0]
final_value_of_ret = 0
for val_second in values2:
    # print(val)
    get_in_2 = values2.index(val_second)
    # print(get_in)
    if get_in_2 == 0:
        new_array_of_return.append(val_second)
    else:
        for o in range(0, get_in_2 + 1):
            final_value_of_ret = final_value_of_ret + values2[o]
        new_array_of_return.append(final_value_of_ret)
        final_value_of_ret = 0
# print(new_array_of_return)

x = range(len(cumulative_target_that_needs_to_plot))
xx = range(len(new_array))

list_index_for_target = len(cumulative_target_that_needs_to_plot) - 1
# print(list_index_for_target)

list_index_for_sale = len(new_array) - 1
# print(list_index_for_sale)
fig, ax = plt.subplots(figsize=(13.5, 4.3),facecolor='#eaeaea')
plt.fill_between(x, cumulative_target_that_needs_to_plot, color="#2fa8a4", alpha=1)
plt.plot(xx, new_array, color="#113d3c", linewidth=3, linestyle="-")
plt.plot(xx, new_array_of_return, color="red", linewidth=3, linestyle="-")

# plt.text(list_index_for_sale-1, cumulative_target_that_needs_to_plot[list_index_for_sale]+6, format(round(cumulative_target_that_needs_to_plot[list_index_for_sale],1),',') + ' Cr',
#          color='black', fontsize=15, fontweight='bold')
plt.scatter(list_index_for_sale, cumulative_target_that_needs_to_plot[list_index_for_sale], s=60, facecolors='#113d3c', edgecolors='white')
plt.text(list_index_for_sale+.2, new_array[list_index_for_sale]+1, format(round(new_array[list_index_for_sale],1),',') + ' Cr',
         color='black', fontsize=15, fontweight='bold')
plt.scatter(list_index_for_sale, new_array[list_index_for_sale], s=60, facecolors='#113d3c', edgecolors='white')

plt.text(list_index_for_sale+.2, new_array_of_return[list_index_for_sale]+1, format(round(new_array_of_return[list_index_for_sale],1),',') + ' Cr',
         color='black', fontsize=15, fontweight='bold')
plt.scatter(list_index_for_sale, new_array_of_return[list_index_for_sale], s=60, facecolors='red', edgecolors='white')

plt.text(list_index_for_target-2, cumulative_target_that_needs_to_plot[list_index_for_target]+6, format(round(cumulative_target_that_needs_to_plot[list_index_for_target],1),',') + ' Cr',
         color='black', fontsize=15, fontweight='bold')
plt.scatter(list_index_for_target, cumulative_target_that_needs_to_plot[list_index_for_target], s=60, facecolors='#113d3c', edgecolors='white')

ax.yaxis.set_visible(False)
ax.set_facecolor("#eaeaea")
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.rcParams['savefig.facecolor'] = '#eaeaea'
plt.tight_layout()
plt.savefig("Cumulative_Day_Wise_Target_vs_Sales.png")
# plt.show()
# plt.close()
print('7. Cumulative day wise target sales')