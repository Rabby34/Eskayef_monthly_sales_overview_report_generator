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

top5_brand_df = pd.read_sql_query("""Select  top 10 b.NAMECUST,c.NAMECUST_ShortName as shortname,a.ret/1000 as returnamount from
(Select CUSTOMER,ISNULL(sum(case when TRANSTYPE<>1 then EXTINVMISC  *-1 end), 0) as ret from OESalesDetails
group by CUSTOMER) as a
left join
(Select IDCUST,NAMECUST from CustomerInformation
group by IDCUST,NAMECUST) as b
on b.IDCUST = a.CUSTOMER
left join
(select IDCUST,NAMECUST_ShortName from Customer_ShortName
group by IDCUST,NAMECUST_ShortName) as c
on b.IDCUST = c.IDCUST
group by b.NAMECUST,c.NAMECUST_ShortName,a.ret
having a.ret<>0
order by a.ret DESC""", connection)

Brand_name = top5_brand_df['shortname'].values.tolist()
sales_values = top5_brand_df['returnamount'].values.tolist()

frequencies = sales_values

frequencies.reverse()

freq_series = pd.Series(frequencies)

y_labels = Brand_name

colors=['#3ea4e3','#3ea4e3','#3ea4e3','#3ea4e3','#3ea4e3']

#colors.reverse()
# Plot the figure.
plt.figure(figsize=(5.1, 6.8),facecolor='#eaeaea')
ax = freq_series.plot(kind='barh',width=.4,color=colors)
#ax.set_title('Amount Frequency')
ax.set_xlabel('Frequency')
ax.set_ylabel('Amount ($)')
ax.set_yticklabels(y_labels)
#ax.set_xlim(0, 300) # expand xlim to make labels easier to read

rects = ax.patches

# For each bar: Place a label
i=0
for rect in rects:
    # Get X and Y placement of label from rect.
    x_value = rect.get_width()#/2
    y_value = rect.get_y() + rect.get_height() / 2

    # Number of points between bar and label. Change to your liking.
    space = 0
    # Vertical alignment for positive values
    ha = 'left'

    # If value of bar is negative: Place label left of bar
    if x_value < 0:
        # Invert space to place label to the left
        space *= -1
        # Horizontally align label at right
        ha = 'right'

    # Use X value as label and format number with one decimal place
    label = "{:.1f}".format(frequencies[i])+'k'
    i=i+1
    # Create annotation
    plt.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',color='black',  # Vertically center label
        fontsize=12,fontweight='bold',ha=ha)                      # Horizontally align label differently for
                                    # positive and negative values.

plt.axis('off')
plt.rcParams['savefig.facecolor'] = '#eaeaea'
#plt.show()
plt.savefig("./chemist_bar_with_value.png")

print('only chemist bar generated without values')