'''
Question 1.
    "99 Bottles of Beer 
    
    "Create a function that accepts any integer as a parameter.
    "The function will take that parameter and use a loop to print the following message: 
    "#bottles of beer on the wall, take one down, pass it around (where # is the parameter value). 
    "The message will be printed starting with the number given as an argument to the function, down to 
   "Once the loop ends, print No bottles of beer on the wall. You must call the function as part of your answer.
'''


def beers(beers):
  print(f'{beers} beers on the wall')
  
  while beers > 0:
    print(f'{beers} beers on the wall, {beers} bottles of beer. Take one down, pass it around ')
    beers -= 1
 print('No bottles of beer on the wall')

beers(int(input('How many beers on the wall?')))

'''
Question 2

Create a function that will accept 3 integers as parameters; those integers will be 
used as the angles of a triangle and must add up to 180. If the arguments supplied to your 
function do not add up to 180, output an error message. Otherwise, your function should be able 
to determine, and output, whether the triangle is a right triangle (one 90 degree angle), an acute 
triangle (all angles less than 90 degrees), or an obtuse triangle (one angle greater than 90 degrees). 
You must call the function as part of your answer. No user input is needed

'''
def triangle(x,y,z):
  if x+y+z != 180:
    print('The angles must ad up to 180!')
   else:
    if x == 90 or y == 90 or z == 90:
      print('This is a Right Triangle')
    elif x < 90 and y < 90 and z < 90:
      print('This is is an Acute Triangle')
    elif x > 90 or y > 90 or z > 90:
      print('This is an Obtuse Triangle')
triangle(60,20,100)

'''
Question 3
Create a program that asks the user for 2 pieces of data:

An amount of money
Type of currency (limit the acceptable types of currency to USD and Mexican Pesos)
As part of your program, you will create a function that accepts an integer and a string as parameters. 
If the user inputs an amount in USD, your function should output the amount in Mexican Pesos; if your user inputs an 
amount in Mexican Pesos, the output should be in USD. When calling the function, the user input should be used as arguments 
(do not hard code the amount of money or currency type). 
You must call the function as part of your answer. You can do a google search to find the correct conversion rates.

'''
def converter(currency,amount):
   
    if currency == 'USD':
        result = amount*18.01
        print(f'You get {result} Pesos')
    elif currency == 'Peso':
        result = amount*0.056
        print(f'You get {result} dollars')
       
converter(input('what is your currency USD/Peso? '), int(input('What is your amount?')))

'''
Question 4

Farmer Dan keeps 2 kinds of livestock: chickens, cows. Write a program that will allow the Farmer to 
input a number of legs for each type of animal and have the appropriate number of heads output. The following constraints must be in place:

An odd number of legs cannot be entered for either type of animal
A number that is not divisible by 2 cannot be entered for chicken legs (entering 0 is allowed)
A number that is not divisible by 4 cannot be entered for cow legs (entering 0 is allowed)
If the user attempts to do any of the above, they should be prompted to try again; the program should not stop abruptly.
Once the user has completed the inventory and the correct counts are returned the program should end. You do not have to 
ask the user if they want to take another inventory.
'''
chicken = 0
cow = 0

animal = input('what animal? ')

if animal == 'cow':
    legs = int(input('how many legs? '))

    while legs%2!=0 or legs%4!=0:
        legs = int(input('enter the right amount of legs: '))
       
    cow += legs + cow
    print(f"you got {cow/4} cows")
                         
     

if animal == 'chicken':
    legs = int(input('how many legs? '))
       
    while legs%2!=0:
        legs = int(input('enter the right amount of legs: '))
       
    chicken += legs + chicken
    print(f"you got {chicken/2} chicken")
