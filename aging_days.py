import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from datetime import datetime
import os

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=;'                     # Provide server
                        'DATABASE=;'                   # provide database 
                        'UID=;PWD=')                   # provide username and password

def numberInCrore(number):
    number = number / 10000000
    number = round(number,2)
    number = format(number, ',')
    number = number + 'Cr'
    return number

CloseTo_mature_df = pd.read_sql_query(""" select  CASE
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=30 THEN '30 Days'
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>30 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=45 THEN '45 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>45 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=60 THEN '60 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>60 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=90 THEN '90 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>90 THEN '90+ Days'
    ELSE 'Over 90'
END 

as aging,sum(OUT_NET) as outstanding
from cust_out
group by 
 CASE
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=30 THEN '30 Days'
    WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>30 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=45 THEN '45 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>45 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=60 THEN '60 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>60 
 and DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )<=90 THEN '90 Days'
   WHEN DATEDIFF(day,convert(datetime, convert(varchar(10), INVDATE), 112),Getdate() )>90 THEN '90+ Days'
    ELSE 'Over 90'
END 
order by aging ASC""",connection)



# print(CloseTo_mature_df.head())

AgingDays = CloseTo_mature_df['aging']
width = 0.6
y_pos = np.arange(len(AgingDays))
performance = CloseTo_mature_df['outstanding']

tovalue = sum(performance)
maf_kor = max(performance)
fig, ax = plt.subplots(figsize=(5, 3),facecolor='#eaeaea')
bars = plt.bar(y_pos, performance, width, align='center', alpha=1,color=['#db9690','#c86057','#b2443a','#782e27','#3e1814'])

# bars[0].set_color('#f00228')
# bars[1].set_color('#ff6500')
# bars[2].set_color('#deff00')
# bars[3].set_color('#2c8e14')


def autolabel(bars):
    for bar in bars:
        height = int(bar.get_height())
        ax.text(bar.get_x() + bar.get_width() / 2., height+22000000,
                str(numberInCrore(height)),
                ha='center', va='bottom', fontsize=12, rotation=0, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width() / 2., height+3000000,
                '(' + str(round(((height / tovalue) * 100), 1)) + "%)",
                ha='center', va='bottom',color='#131a7f', fontsize=10, rotation=0, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width() / 2., height + 3000000,
                '(' + str(round(((height / tovalue) * 100), 1)) + "%)",
                ha='center', va='bottom', color='#131a7f', fontsize=10, rotation=0, fontweight='bold')

autolabel(bars)

#
# def autolabel2(bars):
#     for bar in bars:
#         height = int(bar.get_height())
#         ax.text(bar.get_x() + bar.get_width() / 2., .5 * height,
#                 str(round(((height / tovalue) * 100), 1)) + "%",
#                 ha='center', va='bottom', fontsize=10, fontweight='bold',color='white')
#
#
# autolabel2(bars)

# plt.xticks(y_pos, AgingDays, fontsize=12)
# plt.yticks(np.arange(0, maf_kor + (.6 * maf_kor), maf_kor / 5), fontsize=12)
# plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
# plt.yticks(np.arange(0, round(ran) + (.6 * round(ran))), fontsize='12')
# plt.ylabel('Amount', color='black', fontsize=14, fontweight='bold')
plt.axis('off')

# ax.yaxis.set_visible(False)
# ax.set_facecolor("#a1efea")
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(True)
# plt.title('Total Ageing', color='#3e0a75', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.rcParams['savefig.facecolor'] = '#eaeaea'
plt.savefig('aging_outstanding.png')
# plt.show()
print(' aging Generated')