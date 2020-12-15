# Bring some raw data.
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

# top5_brand_df = pd.read_sql_query("""select top 5 prinfoskf.BRAND as BRAND,ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0) as returnA,
# ISNULL(sum(case when TRANSTYPE=1 then EXTINVMISC  end), 0) as salesA,
# ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0)
# /ISNULL(sum(case when TRANSTYPE=1 then EXTINVMISC  end), 0)*100 as ReturnPercent
#  from OESalesDetails,PRINFOSKF
# where OESalesDetails.ITEM=PRINFOSKF.itemno and
# LEFT(OESalesDetails.TRANSDATE,6) = left(convert(varchar(6), GETDATE(),112),6)
# group by prinfoskf.BRAND
# having sum(case when TRANSTYPE=1 then EXTINVMISC  end)<>0
# order by ReturnPercent DESC""", connection)
#
# Brand_name = top5_brand_df['BRAND'].values.tolist()
# sales_values = top5_brand_df['ReturnPercent'].values.tolist()
sales_values=[10,90,80,40,70,80,85,65,90,45,100]
frequencies = sales_values

frequencies.reverse()

freq_series = pd.Series(frequencies)

# y_labels = Brand_name

colors=['#eaeaea','#FF006E','#FF006E','#FF006E','#FF006E','#FF006E','#FF006E','#FF006E','#FF006E','#FF006E','#FF006E']

#colors.reverse()
# Plot the figure.
plt.figure(figsize=(3, 4.5),facecolor='#eaeaea')
ax = freq_series.plot(kind='barh',width=.4,color=colors)
#ax.set_title('Amount Frequency')
ax.set_xlabel('Frequency')
ax.set_ylabel('Amount ($)')
# ax.set_yticklabels(y_labels)
#ax.set_xlim(0, 300) # expand xlim to make labels easier to read

rects = ax.patches

# # For each bar: Place a label
# i=0
# for rect in rects:
#     # Get X and Y placement of label from rect.
#     x_value = rect.get_width()#/2
#     y_value = rect.get_y() + rect.get_height() / 2
#
#     # Number of points between bar and label. Change to your liking.
#     space = 0
#     # Vertical alignment for positive values
#     ha = 'left'
#
#     # If value of bar is negative: Place label left of bar
#     if x_value < 0:
#         # Invert space to place label to the left
#         space *= -1
#         # Horizontally align label at right
#         ha = 'right'
#
#     # Use X value as label and format number with one decimal place
#     label = "{:.1f}".format(frequencies[i])+'%'
#     i=i+1
#     # Create annotation
#     plt.annotate(
#         label,                      # Use `label` as label
#         (x_value, y_value),         # Place label at end of the bar
#         xytext=(space, 0),          # Horizontally shift label by `space`
#         textcoords="offset points", # Interpret `xytext` as offset in points
#         va='center',color='black',  # Vertically center label
#         fontsize=8,fontweight='bold',ha=ha)                      # Horizontally align label differently for
#                                     # positive and negative values.

plt.axis('off')
plt.rcParams['savefig.facecolor'] = '#eaeaea'
# plt.gca().invert_xaxis()
plt.tight_layout()
# plt.show()
plt.savefig("right_mirror.png")

print('right morror generated')