# task 1

'''
Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
'''

crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)

# Preview the DataFrame to confirm the new column is correct
print(crimes.head())

# Produce a countplot to find the largest frequency of crimes by hour
sns.countplot(data=crimes, x="HOUR OCC",color='black')
plt.title('Largest Frequency of Crimes by Hour')
plt.show()

crimes['US TIME'] = pd.to_datetime(crimes['TIME OCC'], format='%H%M')
crimes['US TIME'] = crimes['US TIME'].dt.strftime('%I:%M %p')
hour_counts = crimes['US TIME'].value_counts()
peak_crime_hour = hour_counts.head(1).index[0].strip()
print('Hour that has highest frequency of crimes is: ',peak_crime_hour)


# task 2
'''
Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called peak_night_crime_location.
'''
crimes.head()
peak_night_crime_location_time = crimes[(crimes['TIME OCC']<'0359') | (crimes['TIME OCC']>'2200')]

sns.countplot(x='AREA NAME', data=peak_night_crime_location_time, color='black')

plt.xticks(rotation='vertical')
plt.title('Area of Night Time Crime Occurrences')
plt.xlabel('Hour')
plt.ylabel('Count')
plt.show()

peak_night_crime_location = peak_night_crime_location_time['AREA NAME'].value_counts().head(1).index[0]
print('Area that has the largest frequency of night crimes is: ',peak_night_crime_location)

# task 3
'''
Identify the number of crimes committed against victims by age group (<18, 18-25, 26-34, 35-44, 45-54, 55-64, 65+). Save as a pandas Series called victim_ages.
'''
bins = [0, 18, 25, 34, 44, 54, 64, float('inf')]
labels = ['<18', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']

# Create a new column 'Age Group' based on the bins
crimes['Age Group'] = pd.cut(crimes['Vict Age'], bins=bins, labels=labels, right=False)

# Count occurrences within each age group
victim_ages = crimes['Age Group'].value_counts()
victim_ages = pd.DataFrame(victim_ages).rename_axis('Age Group').rename(columns={'Age Group': 'Count'})
print(victim_ages)
