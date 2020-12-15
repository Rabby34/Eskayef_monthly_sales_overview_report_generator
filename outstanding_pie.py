import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from datetime import datetime
import os

conn = db.connect('DRIVER={SQL Server};'
                        'SERVER=;'                     # Provide server
                        'DATABASE=;'                   # provide database 
                        'UID=;PWD=')                   # provide username and password

def numberInCrore(number):
    number = number / 10000000
    number = round(number,2)
    number = format(number, ',')
    number = number + ' Cr'
    return number

outstanding_df = pd.read_sql_query(""" select
                    SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
                    SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit
                    from  [ARCOUT].dbo.[CUST_OUT]
                    where [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)

                     """, conn)

cash = int(outstanding_df['TotalOutStandingOnCash'])
credit = int(outstanding_df['TotalOutStandingOnCredit'])

data = [cash, credit]
total = cash + credit
total = 'Total \n' + numberInCrore(total)

colors = ['#031F4B', '#6497B1']
fig, ax = plt.subplots(figsize=(8, 4),facecolor='#eaeaea', subplot_kw=dict(aspect="equal"))

recipe = ["Cash   \n "+str(numberInCrore(cash)),
          "  Credit\n"+str(numberInCrore(credit))]


wedges, texts ,autopct= ax.pie(data, wedgeprops=dict(width=0.4), startangle=90,colors=colors, autopct='%.1f%%', textprops={
        'color':"white"},pctdistance=.8)

plt.setp(autopct, fontsize=12, fontweight='bold')

ax.text(0, -.1, total, ha='center', fontsize=13, fontweight='bold',color='#571845')

bbox_props = dict(boxstyle="square,pad=0.3", fc='y', ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center",fontsize=13,fontweight='bold')

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.5*np.sign(x), 1.3*y),
                horizontalalignment=horizontalalignment, **kw)
plt.title('Total Outstanding', fontsize=16, fontweight='bold', color='black')
plt.rcParams['savefig.facecolor'] = '#eaeaea'
plt.tight_layout()
# plt.show()
plt.savefig('./outstanding_donut.png', transparent=False)
print('outstanding circle generated')