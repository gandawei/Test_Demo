import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib as mlt
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})

file=pd.read_csv('./lianjia.csv')
df = file.copy()

df['PerPrice'] = file['Price']/file['Size']
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation', 'PerPrice', 'Price']

df=DataFrame(df,columns=columns)

#print(df.head(100))

df_house_count=df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()

df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2,ax3] = plt.subplots(3,1,figsize=(18,12))
sns.barplot(x='Region', y='PerPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
ax1.set_title('北京各大区二手房每平米单价对比',fontsize=15)
ax1.set_xlabel('区域')
ax1.set_ylabel('每平米单价')

sns.barplot(x='Region', y='Price', palette="Greens_d", data=df_house_count, ax=ax2)
ax2.set_title('北京各大区二手房数量对比',fontsize=15)
ax2.set_xlabel('区域')
ax2.set_ylabel('数量')

sns.boxplot(x='Region', y='Size', data=df, ax=ax3)
ax3.set_title('北京各大区二手房房屋总价',fontsize=15)
ax3.set_xlabel('区域')
ax3.set_ylabel('房屋总价')


df= df[(df['Layout']!='叠拼别墅') & (df['Size']<1000) ]
f, [ax1,ax2,ax3] = plt.subplots(1, 3, figsize=(15, 5))
sns.distplot(df['Size'], ax=ax1, color='r')
sns.regplot(x='Size', y='Price', data=df, ax=ax2)
sns.distplot(df['Size'],ax=ax3,kde=False,bins=[x for x in range(4)])
#sns.kdeplot(df['Size'], shade=True, ax=ax1)

f,ax1=plt.subplots(figsize=(20,20))
sns.countplot(y='Renovation',data=df,ax=ax1)
ax1.set_title('房屋户型',fontsize=8)
ax1.set_xlabel('数量')
ax1.set_ylabel('户型')
plt.show()

