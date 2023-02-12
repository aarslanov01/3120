'''
Create a program that allows the user to order from a menu of 6 items with prices as follows:
Penne alla vodka - $15.00
Falafel sandwich - $13.99
Chicken biryani - $20.75
Xiaolongbao - $10.25
Coca-cola - $0.75
Water - $1.25

'''

print("Welcome to Ainur's Bar!")
print('')
print('Menu')
print('____')
print('1.Penne alla vodka - $15.00 ')
print('2.Falafel sandwich - $13.99 ')
print('3.Chicken biryani - $20.75 ')
print('4.Xiaolongbao - $10.25 ')
print('5.Coca-cola - $0.75 ')
print('6.Water - $1.25 ')

#set counters for each items
ch1 = 0
ch2 = 0
ch3 = 0
ch4 = 0
ch5 = 0
ch6 = 0

# set counters for subtotal including taxes
total = 0
tax = 0
tip = 0
subtotal = 0

print()
print('Please input the quantity for each item you would like to order')


#assign the input
pav = int(input('Penne alla vodka'))
print(f'Penne alla vodka: {pav}')
# append the input times price to the relevant counters
ch1 += pav*15

fs = int(input('Falafel sandwich'))
print(f'Falafel sandwich: {fs}')
ch2 += fs*13.99

cb = int(input('Chicken biryani'))
print(f'Chicken biryani: {cb}')
ch3 += cb*20.75

x = int(input('Xiaolongbao'))
print(f'Xiaolongbao: {x}')
ch4 += x*10.25

cc = int(input('Coca-cola'))
print(f'Coca-cola {cc}')
ch5 += cc*.75

w = int(input('Water'))
print(f'Water: {w}')
ch6 += w*1.25

total += (ch1+ch2+ch3+ch4+ch5+ch6)
tax += .0825*total

print('')
print('Reciept')
print('_______')

#build the logical structure to eliminate the items with 0 choice 
if ch1> 0: 
    print(f'Penne alla vodka: ${ch1}')
if ch2> 0:
    print(f'Falafel sandwich: ${ch2}')

if ch3>0:
    print(f'Chicken biryani: ${ch3}')

if ch4>0:
    print(f'Xiaolongbao: ${ch4}')

if ch5>0:
    print(f'Coca-cola: ${ch5}')

if ch6> 0:
    print(f'Water: ${ch6}')

print(f'Subtotal: ${total}')
print(f'Tax: ${round(tax,2)}')
print('')
print('Enter a Tip amount')
print(f'15% - ${round((total*.15),2)}')
print(f'20% - ${round((total*.25),2)}')
print(f'25% - ${round((total*.20),2)}')

#calculate teh tips and subtotal over the counters 
tip = int(input(''))
subtotal += total + tax + (tip/100)*total 

#end the program
print('')
print(f'TOTAL: ${round(subtotal,2)}')
print('DANKE!')
