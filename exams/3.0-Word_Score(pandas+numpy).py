'''
Create a Series that contains letter and corresponding point values according to the following:
- 1 point: E, A, I, O, N, R, T, L, S, U
- 2 points: D, G
- 3 points: B, C, M, P
- 4 points: F, H, V, W, Y
- 5 points: K
- 8 points: J, X
- 10 points: Q, Z

Using the Series, create a program that allows the user to enter a word and have the total point 
value of the word returned. The program must allow the user to continue to enter words until they decide 
to exit the program.

'''
import pandas as pd
import numpy as np

# Step 1 create a dictionaries with corresponding values
one_p = {}
letters = ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']
for letter in letters:
    one_p[letter] = 1
print(one_p)
one_p_s = pd.Series(one_p)

two_p = {}
letters = ['D','G']
for letter in letters:
    two_p[letter] = 2
print(two_p)
two_p_s = pd.Series(two_p)

three_p = {}
letters = ['B','C','M','P']
for letter in letters:
    three_p[letter] = 3
print(three_p)
three_p_s = pd.Series(three_p)

four_p = {}
letters = ['F','H','V','W','Y']
for letter in letters:
    four_p[letter] = 4
print(four_p)
four_p_s = pd.Series(four_p)

five_p = {}
letters = ['K']
for letter in letters:
    five_p[letter] = 5
print(five_p)
five_p_s = pd.Series(five_p)

eight_p = {}
letters = ['J','X']
for letter in letters:
    eight_p[letter] = 8
print(eight_p)
eight_p_s = pd.Series(eight_p)

ten_p = {}
letters = ['Q','Z']
for letter in letters:
    ten_p[letter] = 10
print(ten_p)
ten_p_s = pd.Series(ten_p)

# Step 2. Create series 
point_series = pd.concat([one_p_s,two_p_s,three_p_s,four_p_s,five_p_s,eight_p_s,ten_p_s])
print()
print(point_series)


# word prompt and point calculation 
run = str(input('to run: R, to quit enter: Q: ')).upper()

while run == 'R':
    total_points = 0
    word = str(input('give me a word: ')).upper()
    print(f'your words is {word}')
    word_letters = list(word)
    for l in word_letters:
        if l in point_series:
            total_points += point_series[l]
    print('total points:', total_points)
    run_check = str(input('to run: R, to quit enter: Q: ')).upper()
    run = run_check


print('\nthx bye!')
        
