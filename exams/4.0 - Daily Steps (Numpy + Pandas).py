'''
### 3. Daily Step Stats
Create a program that allows a user to enter their daily step count, 7 days at a time (exactly 7, do not give the option to enter less). For the first 7 days of user input, create a NumPy array of steps and output the array and the following:
1. The total number of steps for all 7 days
2. The average number of steps taken
3. The number of miles walked eached day (1 mile = 2000 steps)
4. The total number of miles for all 7 days
5. The highest step count during the 7 days

Allow the user to enter additional weeks, 7 days at a time. Reshape the NumPy array for each 7 day period added; i.e for the first 7 days the array should be 1 dimensional, for the second, the array shape of the array should be (2,7), etc. After data for each new week is entered, output the updated array and the following:
1. The total number of steps for x days, where x is the size of the array
2. The average number of steps taken, both for each week and overall
3. The number of miles walked eached day
4. The total number of miles for each week
5. The total number of miles for all days
6. The highest step count for each week
7. The highest step count overall
'''

import pandas as pd
import numpy as np

status = input('Start enter: [S], Quit enter: [Q]').upper()
week_counter = 1
while status == 'S':
    # dictionary to hold the days
    daily_steps = {}
    week = {}
    

    # ask for the step input
    print(f'lets calculate week {week_counter}')
    for day in range(1,8):
        steps = int(input(f'steps for day {day} in week {week_counter}: '))
        week[f'Day {day}'] = steps
    daily_steps[f'week {week_counter}'] = week
    

    # convert the dict into an array
    print(daily_steps)
    values = list(daily_steps.values())
    steps_array = np.array([val for inner_dict in daily_steps.values() for val in inner_dict.values()])
    print()
    print(steps_array)

    
    # reestablish the status
    new_status = input('Continue enter: [S], Quit enter: [Q]').upper()
    status = new_status

    #calculate the stats
    # total steps
    total = steps_array.sum()
    # average
    average = steps_array.mean()

    # miles 
    daily_miles = {}

    for day, steps in week.items():
        daily_miles[f'Miles for {day}'] = steps/2000
            
    # total number of miles for 7 days
    total_miles = total/2000

    #highest step count
    highest = steps_array.max()
        

    # output the statistics
    print()
    print('stats for week:',week_counter)
        
    print('total count:',total)
    print('average number of steps: ',average)
    print('miles per day: ')
    for day, mile in daily_miles.items():
        print(day,':',mile,'miles')
    print('total miles:',total_miles)
    print('max amount steps you did during the 7 days:',highest)
    week_counter += 1
    

    
    

print('thanks bye')
