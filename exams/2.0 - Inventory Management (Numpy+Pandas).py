'''
Create a DataFrame that contains the beginning inventory for a hot dog stand: 20 hot dogs, 
20 cans of coke, 20 bottles of water and 10 soft pretzels. Each time a sale is made, the user
will enter the quantity of items sold and the DataFrame will be updated to reflect the new available 
inventory. Output the updated DataFrame after each update. The program must allow the user to continue 
to enter sales until all the items are sold. Once an item's inventory has been depleted, print a message
notifying the user that the item can no longer be sold. If the user tries to record the sale of an item after 
its inventory has been depleted, print a message alerting the user to their mistake. 
Once all the items have been depleted, print "All items have been sold" and exit the program.
'''
import pandas as pd
import numpy as np

items = ['hot dog', 'coke', 'water', 'pretzels']
qty = [20,20,20,10]

df_inventory = pd.DataFrame({'items': items, 'qty': qty})

print('See the menu:\n')
print(df_inventory)



while df_inventory['qty'].sum() > 0:
    item = input('what would you like to purchase? ').lower()
    result = df_inventory.loc[df_inventory['items'] == item]
    result_qty = result['qty'].tolist()[0]
    if not result.empty:
        print(f'we got {item} in qty of {result_qty}')
        order_amount = int(input('how many you want to order? \n'))
        while order_amount > result_qty: 
            print('Your request exceeds the amount\n')
            order_amount = int(input('how many you want to order? \n'))
            
        if order_amount <= result_qty:
            result_qty -= order_amount
            print(f'here is your {item}\n')
            df_inventory.loc[df_inventory['items'] == item,'qty'] = result_qty
            print(df_inventory)
            result = df_inventory.loc[df_inventory['items'] == item]
            result_qty = result['qty'].tolist()[0]
            if result_qty == 0:
                print()
                print(f'we are out of {item}')
                
            else: 
                print(f'we still have some {item} left')
       
    else: 
        print('we dont have it')
        
if df_inventory['qty'].sum() == 0:
    print('we got nothing left')
    print('thanks for visiting us ')
