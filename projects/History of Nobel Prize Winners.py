# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# task 1
'''
What is the most commonly awarded gender and birth country? Storing the string answers as top_gender and top_country
'''
nobel_df = pd.read_csv('data//nobel.csv')
nobel_df.head()
top_gender = nobel_df['sex'].value_counts().head(1)
top_country = nobel_df['birth_country'].value_counts().head(1)
print('the gender with most laureates is:', top_gender.index.tolist()[0])
print('the country with most laureates is:', top_country.index.tolist()[0])

# task 2
'''
What decade had the highest proportion of US-born winners? Store this as an integer called max_decade_usa
'''
nobel_df.head()
nobel_decade_df = (nobel_df['year']//10)*10
nobel_df['decade'] = nobel_decade_df
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
max_decade_usa = nobel_df[(nobel_df['birth_country'] == 'United States of America') | (nobel_df['birth_country'] == 'USA') ]['decade'].value_counts().index.tolist()[0]
print('decade that had the highest proportion of US-born winners is: ',max_decade_usa)


# task 3
'''
What decade and category pair had the highest proportion of female laureates? Store this as a dictionary called max_female_dict where the decade is the key and the category is the value.
'''
nobel_df.head()
max_female_dict = nobel_df[nobel_df['sex']=='Female'][['decade','category']].value_counts().index.tolist()[0]
print()
print(max_female_dict)

# task 4
'''
Who was the first woman to receive a Nobel Prize, and in what category? Save your string answers as first_woman_name and first_woman_category
'''
first_woman_name = nobel_df[nobel_df['sex']=='Female'].sort_values(by='year',ascending=True)['full_name'].head(1)
print('first woman name is:',first_woman_name.to_string(index=False))
first_woman_category = nobel_df[nobel_df['sex']=='Female'].sort_values(by='year',ascending=True)['category'].head(1)
print()
print('first woman category is:',first_woman_category.to_string(index=False))

# task 5
'''
Which individuals or organizations have won multiple Nobel Prizes throughout the years? Store the full names in a list named repeat_list
'''

nobel_df.head()
#nobel_df['laureate_type'].value_counts()
#nobel_df[nobel_df['full_name'].isin(nobel_df['full_name'].value_counts()[nobel_df['full_name'].value_counts() > 1].index)]
repeat_list = nobel_df[nobel_df['full_name'].isin(nobel_df['full_name'].value_counts()[nobel_df['full_name'].value_counts()>1].index)]['full_name'].unique()
print()
print(repeat_list)
