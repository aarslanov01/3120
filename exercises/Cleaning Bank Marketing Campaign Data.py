import pandas as pd
import numpy as np

bank_marketing_df = pd.read_csv('bank_marketing.csv')
bank_marketing_df.head()

# Data cleaning
'''
client.csv

client_id
age
job: Change "." to "_"
marital
education: Change "." to "_" and "unknown" to np.NaN
credit_default: Convert to boolean data type
mortgage: Convert to boolean data type

'''
client = pd.DataFrame()
client['client_id'] = bank_marketing_df['client_id']
client['age'] = bank_marketing_df['age']
client['job'] = bank_marketing_df['job'].str.replace('.','_')
client['marital'] = bank_marketing_df['marital']
client['education'] = bank_marketing_df['education'].str.replace('.','_').replace('unknown',np.NaN)
client['credit_default'] = bank_marketing_df['credit_default'].astype(bool)
client['mortgage'] = bank_marketing_df['mortgage'].astype(bool)

'''
campaign.csv

client_id: N/A
number_contacts: N/A
contact_duration: N/A
previous_campaign_contacts: N/A
previous_outcome: Convert to boolean data type
campaign_outcome: Convert to boolean data type
last_contact_date: Create from a combination of day, month, and a newly created year column (which should have a value of 2022);
Format = "YYYY-MM-DD"
'''
campaign = pd.DataFrame()
campaign['client_id'] = bank_marketing_df['client_id']
campaign['number_contacts'] = bank_marketing_df['number_contacts']
campaign['contact_duration'] = bank_marketing_df['contact_duration']
campaign['previous_campaign_contacts'] = bank_marketing_df['previous_campaign_contacts']
campaign['previous_outcome'] = bank_marketing_df['previous_outcome'].astype(bool)
campaign['campaign_outcome'] = bank_marketing_df['campaign_outcome'].astype(bool)
bank_marketing_df['year'] = 2022

# covert the month to date time object
def month_name_to_number(month_name):
    month_datetime = pd.to_datetime(month_name, format='%b')
    return month_datetime.strftime('%m')

# Apply the function to the 'month' column
bank_marketing_df['month'] = bank_marketing_df['month'].apply(month_name_to_number)

# create 'last_contact'
campaign['last_contact'] = pd.to_datetime(bank_marketing_df[['year','month','day']].astype(str).agg('-'.join,axis=1),format='%Y-%m-%d')

'''
economics.csv

client_id: N/A
cons_price_idx: N/A
euribor_three_months: N/A
''' 
economics = pd.DataFrame()
economics['client_id'] = bank_marketing_df['client_id']
economics['cons_price_idx'] = bank_marketing_df['cons_price_idx']
economics['euribor_three_months'] = bank_marketing_df['euribor_three_months']

# Finally save the cleaned dataframes

client.to_csv('client.csv',index=False)
campaign.to_csv('campaign.csv',index=False)
economics.to_csv('economics.csv',index=False)
campaign.head()
