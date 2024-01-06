import numpy as np
import pandas as pd
import random as rd
#Create a 10x10 array of zeros with the int datatype. Using slicing, assign the value 1 to the outermost elements of the array.**
x = np.ones((10,10), dtype=int)
x[1:-1, 1:-1] = 0
x
#Create a new 10x10 array of random numbers. Using the NumPy min and max functions, calculate and print the mathematical range of the entire array (the result should only be one number, not an array).**
y = np.random.randint(1,100,(10,10))
print('here is the array:\n',y)
my_range = y.max() - y.min()
print()
print('here is the range: ',my_range)
#Create a 12x12 array of ones. Using a for loop, update the values in the array to produce the following:**
n = np.ones((12,12),dtype = int)
value = 1
for x in n: 
    for i in range(len(x)):
        x[i] = value
        value +=1
n
'''
Create a Series using the following pumpkin pie recipe. Use the ingredients as indices and the quantity as the corresponding values.**
- 1 package store-bought pie-crust
- 1 cup light brown sugar
- 1 tablespoon all-purpose flour
- 1/2 teaspoon salt
- 1 teaspoon ground cinnamon
- 1 teaspoon ground ginger
- 1/2 teaspoon ground nutmeg
- 1/8 teaspoon ground cloves
- 3 large eggs
- 15 ounce can pumpkin puree
- 1 1/4 cup evaporated milk
'''
my_series = pd.Series(['1 package','1 cup','1 tablespoon','1/2 teaspoon','1 teaspoon','1 teaspoon','1/2 teaspoon','1/8 teaspoon',3,'15 ounce can', '1/4 cup'], 
                      index=['store-bought pie-crust','light brown sugar','all-purpose flour','salt','ground cinnamon','ground ginger','ground nutmeg','ground cloves','large eggs','pumpkin puree','evaporated milk'])
my_series
#Based on the previous question, display an alphabetized list of ingredients with the first letter of each item capitalized.**
my_list = my_series.index.tolist()
for n in my_list:
    print(n.capitalize())
#Create a new Series. The indices of this Series will be the same as the Series created in question 5; use the index attribute of the existing Series to set the index of the new Series . The corresponding values will be a NumPy array of prices (DO NOT use the NumPy range or random functions to set the prices). Display the Series and use NumPy functions to display the sum of all prices, the average price, the most expensive item/price and the least expensive item/price.**
indicies = ['store-bought pie-crust','light brown sugar','all-purpose flour','salt','ground cinnamon','ground ginger','ground nutmeg','ground cloves','large eggs','pumpkin puree','evaporated milk']
prices = [4.5,1.25,3,0.99,3.5,1.25,5.5,1,2,2.25,4]
my_new_series = pd.Series(prices, index = indicies)
print(my_new_series)
print('total price:', sum(prices))
avg = sum(prices)/len(prices)
print('average price:', avg)
expensive_index = my_new_series.idxmax()
exp_price = my_new_series[expensive_index]
leastexpensive_index = my_new_series.idxmin()
least_price = my_new_series[leastexpensive_index]
print('most expenisve item: ', expensive_index,exp_price)
print('most expenisve item: ', leastexpensive_index,least_price)
**Display the Series in question 6 with all prices marked down 20%**
discount_prices = []
for n in prices:
    x = n-n*.2
    discount_prices.append(x)
my_new_series = pd.Series(discount_prices, index = indicies)
my_new_series
#Create a DataFrame based on the Series in question 6. Add an extra column for Quantity and have the index for the DataFrame start at 1.**
df = pd.DataFrame(my_new_series, columns = ['price'])
df
df['quantity'] = 1
df
'''
Use loc or iloc to set the following quantities:**
- all purpose flour, ground cinnamon, pumpkin puree - 5
- large eggs, light brown sugar, ground ginger - 2
- evaporated milk, ground cloves, ground nutmeg - 3
- salt, store bought pie crust - 4
'''
df.loc[['all-purpose flour','ground cinnamon','pumpkin puree'],'quantity'] = 5
df.loc[['large eggs','light brown sugar','ground ginger'],'quantity'] = 2
df.loc[['evaporated milk','ground cloves','ground nutmeg'],'quantity'] = 3
df.loc[['salt','store-bought pie-crust'],'quantity'] = 4
df
**Add a new column named Total Price to the DataFrame created in question 8. The values for that column should be generated using the Prices and Quantity columns.**
df['total price'] = df.price * df.quantity
df
**Using pandas methods write the DataFrame from question 10 to a .csv file called 'pumpkin-pie-file.csv'**
df.to_csv('pumpkin-pie-file.csv')
