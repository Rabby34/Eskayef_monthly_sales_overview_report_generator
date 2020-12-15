import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import sys

# def convert(number):
#     number = number / 1000
#     number = int(number)
#     number = format(number, ',')
#     number = number + 'K'
#     return number
#
connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=;'                     # Provide server
                        'DATABASE=;'                   # provide database 
                        'UID=;PWD=')                   # provide username and password
#
# cursor = connection.cursor()
#
# total_sales_df = pd.read_sql_query("""Declare @Currentmonth NVARCHAR(MAX);
#                                       SET @Currentmonth = convert(varchar(6), GETDATE(),112);
#                                       select Sum(EXTINVMISC) as  MTDSales from OESalesDetails
#                                       where LEFT(TRANSDATE,6) = @Currentmonth""", connection)
#
# sales = total_sales_df['MTDSales'].values.tolist()
#
# sales_value=sales[0]
#
# total_target_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
#                                       SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
#                                       select ISNULL((Sum(TARGET)), 0) as  MTDTarget from TDCL_BranchTarget
#                                       where YEARMONTH = @CurrentMonth""", connection)
#
# target = total_target_df['MTDTarget'].values.tolist()
#
# target_value=target[0]
#
# achievement=(sales_value/target_value)*100

achievement = 67

data = [achievement, 100-achievement]


colors = ['#E95B54', '#FBCE4A']

# -----------------------------------------------------

fig1, ax = plt.subplots(figsize=(4.2,4.2),facecolor='#eaeaea')
wedges, labels= ax.pie(data,radius=.1, colors=colors, startangle=90)
ax.text(0, -.006, str(round(achievement,1))+'%', ha='center', fontsize=15, fontweight='bold',color='#ff6138')
#
centre_circle = plt.Circle((0, 0), 0.045, fc='#eaeaea')

fig = plt.gcf()

fig.gca().add_artist(centre_circle)

# plt.title('Title of pie', fontsize=16, fontweight='bold', color='#ff6138')

ax.axis('equal')
plt.rcParams['savefig.facecolor'] = '#eaeaea'
plt.tight_layout()
# plt.show()
plt.savefig('mid_pie.png', transparent=False)
print('mid circle generated')