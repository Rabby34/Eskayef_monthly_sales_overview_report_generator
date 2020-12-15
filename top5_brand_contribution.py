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

total_sales_df = pd.read_sql_query("""Declare @Currentmonth NVARCHAR(MAX);   
                                      SET @Currentmonth = convert(varchar(6), GETDATE(),112);
                                      select Sum(EXTINVMISC) as  MTDSales from OESalesDetails  
                                      where LEFT(TRANSDATE,6) = @Currentmonth""", connection)

active_sales = total_sales_df['MTDSales'].values.tolist()

sales_act=active_sales[0]

top_sales_df = pd.read_sql_query("""select top 5 prinfoskf.BRAND as BRAND,Sum(EXTINVMISC) as  MTDSales from OESalesDetails,PRINFOSKF 
	where OESalesDetails.ITEM=PRINFOSKF.itemno and
	LEFT(OESalesDetails.TRANSDATE,6) = left(convert(varchar(6), GETDATE(),112),6) 
	and OESalesDetails.TRANSTYPE=1
	group by prinfoskf.BRAND
	order by MTDSales DESC""", connection)

top_sale = top_sales_df['MTDSales'].values.tolist()

sales_top=sum(top_sale)

data = [sales_top,(sales_act-sales_top)]

percentage_value = (sales_top/sales_act)*100

colors = ['#4f5b1b', '#a9a133']

# -----------------------------------------------------

fig1, ax = plt.subplots(figsize=(3.3,3.3),facecolor='#eaeaea')
wedges, labels= ax.pie(data,radius=.1, colors=colors, startangle=90)
ax.text(0.001, -.005, str(round(percentage_value,1))+'%' , ha='center', fontsize=20, fontweight='bold',color='#4f5b1b')
#
centre_circle = plt.Circle((0, 0), 0.085, fc='#eaeaea')

fig = plt.gcf()

fig.gca().add_artist(centre_circle)

plt.title('Top 5 \nBrand Contribution', fontsize=16, fontweight='bold', color='black')
plt.title('Top 5 \nBrand Contribution', fontsize=16, fontweight='bold', color='black')

ax.axis('equal')
plt.rcParams['savefig.facecolor'] = '#eaeaea'
plt.tight_layout()
# plt.show()
plt.savefig('./customer_order_percentage.png', transparent=False)
print('11. customer order percentage circle generated')

