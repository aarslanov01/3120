'''
### 4. World Happiness
Using the data from the [2019 World Happiness Report](2019.csv), create one figure
containing 3 subplots. The first should plot the Happiness Scores for the top 10 countries. 
The second should plot the Happiness Scores of the bottom 10 countries. Top 10 and bottom 10 should be determined by Happiness Rank, not necessarily the way the data loads from the file. The third should plot the average Happiness Score by Region. Each plot should have an appropriate title, x-/y-axis labels and ticks/tick labels for each axis. Below the figure, 
output the data (as DataFrames) used to create each of the 3 subplots.
'''
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#get the data
df = pd.read_csv('C:/Users/a.arslanov/Downloads/2015.csv')


# #sort highest and lowest ranks
top_10 = df.sort_values(by='Happiness Rank',ascending=False)[:10]
bottom_10 = df.sort_values(by='Happiness Rank',ascending=True)[:10]
print('Top 10 Happiest coutnries are:\n',top_10.loc[:,['Country','Happiness Rank']])
print()
print('Top 10 Unhappiest countries are:\n', bottom_10.loc[:,['Country','Happiness Rank']])

#calculate the average for region
grouped = df.groupby('Region')
mean = grouped['Happiness Rank'].mean()
df_region = pd.DataFrame({'Region': mean.index,'Av.score':mean.values})
print()
print(df_region)

#plot
fig, axes = plt.subplots(nrows=1, ncols=3, figsize = (12,4))
axes[0].barh(top_10['Country'],top_10['Happiness Rank'])
axes[0].set_title('Top 10 Happiest')
axes[0].set_xlabel('Rank')
axes[0].set_ylabel('Countries')

axes[1].barh(bottom_10['Country'], bottom_10['Happiness Rank'])
axes[1].set_title('Top 10 Miserable')
axes[1].set_xlabel('Rank')
axes[1].set_ylabel('Countries')

axes[2].barh(df_region['Region'], df_region['Av.score'])
axes[2].set_title('Average by Region')
axes[2].set_xlabel('Rank')
axes[2].set_ylabel('Countries')

fig.suptitle('Happiness Rank Scores')

plt.tight_layout()
plt.show()
print(top_10)
print()
print(bottom_10)
print()
print(df_region)
