from random import choice
from math import floor
from string import ascii_lowercase

file = open('rating.txt', 'r+')
teste = file.readlines()

for x in range(len(teste)):
    teste[x] = teste[x].replace('\n', '')
for y in range(len(teste)):
    teste[y] = teste[y].split()
for z in range(len(teste)):
    teste[z][1] = int(teste[z][1])

who_wins = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
            'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
            'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
            'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
            'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
            'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
            'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
            'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
            'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
            'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
            'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
            'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
            'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
            'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
            'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}

game_name = input('Enter your name:')
print(f'Hello, {game_name}')
game_rating = 0
for k in range(len(teste)):
    if game_name == teste[k][0]:
        game_rating = teste[k][1]

rules = input()
if rules == '':
    rules = 'rock,paper,scissors'
    rules = rules.replace(',', ' ')
    rules = rules.split()
else:
    rules = rules.replace(',', ' ')
    rules = rules.split()
print("Okay, let's start")

loop = True
while loop == True:
    pc_select = choice(rules)
    player_select = input()
    if player_select == '!rating':
        print(f'Your rating: {game_rating}')
    elif player_select == '!exit':
        print('Bye!')
        loop = False
    elif player_select not in rules:
        print('Invalid input')
    elif 'rock' in rules:
        if pc_select == player_select:
            print(f'There is a draw ({player_select})')
            game_rating += 50
        elif pc_select in who_wins[f'{player_select}']:
            print(f'Well done. Computer chose {pc_select} and failed')
            game_rating += 100
        else:
            print(f'Sorry, but computer chose {pc_select}')
    elif rules != ascii_lowercase:
        metade = floor(len(rules) / 2)
        for x in range(len(rules)):
            if rules[x] == pc_select:
                position = x
        if pc_select == player_select:
            print(f'There is a draw ({player_select})')
            game_rating += 50
        else:
            if position < metade:
                metade_superior = rules[position: position + metade]
                if player_select in metade_superior:
                    print(f'Well done. Computer chose {pc_select} and failed')
                    game_rating += 100
                else:
                    print(f'Sorry, but computer chose {pc_select}')
            elif position >= metade:
                metade_inferior = rules[position - metade:position]
                if player_select in metade_inferior:
                    print(f'Sorry, but computer chose {pc_select}')
                else:
                    print(f'Well done. Computer chose {pc_select} and failed')
                    game_rating += 100
