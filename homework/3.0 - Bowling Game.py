'''
Bowling Game

For this assignment, you will create a bowling game that can be played by an unlimited number of players. To create your game, you will need to do the following:

1. Get the number of players from the user.
2. Get the names of each player from the user and add the names to a list
3. Each player will have 10 rounds; each round consists of 2 rolls. On the first roll, the player can knock down anywhere from 0 to 10 pins. If the user knocks down all 10 pins on the first roll, they don't need a second roll. If the user knocks down fewer than 10 pins on the first roll, they have a chance to knock down the remaining pins on the second roll. The score for each roll is determined by how many pins are knocked down. (Hint: You can put this logic into a function and call the function for each player. Use the random library and randint method to determine the number of pins knocked down on the first and second rolls.)
4. For each round, display the player name, their score for the first roll, and their score for the second roll. Write these 3 pieces of data for each player to a file, as well.
5. Once all rounds are complete, use the file to calculate and display the total score for each player (Hint: You can create a function where the file is opened/closed, and the total calculated. To calculate the total for a particular player, compare the player name in the file to the player name in the list; if the names match, add the scores that correspond to that player. Use a loop to call the function for each player.)
'''

import random

player_name = []
player_number = int(input('how many players are there? '))

for player in range(1,player_number+1):
        player = str(input(f'Player{player}: ')).capitalize()
        player_name.append(player)
        

with open('scores.txt', 'a') as sc:
    for rounds in range(1,11):
        print()
        print(f'Round {rounds}')
        for index, name in enumerate(player_name):
            first = random.randint(0,10)
            second = random.randint(0,10-first)
            score = f'{name}: {first} {second}\n'
            print(score, end='')
            sc.write(f'{name},{first},{second}\n')
            
for p_name in player_name:
    total_score = 0
    
    with open('scores.txt', 'r') as sc:
        for line in sc:
            variables = line.strip().split(',')
            if len(variables) == 3:
                name, bowl1, bowl2 = variables
                if name == p_name:
                    bowl1 = int(bowl1)
                    bowl2 = int(bowl2)
                    total_score += bowl1+bowl2

    print(f'\nTotal score for {p_name} is: ')                
    print(f'{total_score}')
    print()
    
