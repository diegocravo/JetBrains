# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v_tazEygjHzz57O9VuebRa1I6sVPvKLe
"""

from random import choice
from string import ascii_lowercase


lista = ['python', 'java', 'kotlin', 'javascript']
escolha = choice(lista)
alternativa = []
esc1 = list(escolha)
escolhas_feitas = set()

def createLine():
    for x in range(len(escolha)):
        alternativa.append('-')

def imprime():
    final = ''.join(alternativa)
    print('\n')
    print(final)

def initial_msg():
    print('H A N G M A N')

def check_ent():
    if len(letra) > 1 or len(letra) < 1:
        return ('You should print a single letter')
    elif letra not in ascii_lowercase:
        return ('It is not an ASCII lowercase letter')
    elif letra in escolhas_feitas:
        return ('You already typed this letter')
    else:
        return True

initial_msg()
createLine()

tentativas = 1
play = True
while play == True:

    ask = True
    while ask == True:
        ask_continue = input('\nType "play" to play the game, "exit" to quit: ')
        if ask_continue == 'exit':
            play = False
            ask = False
        elif ask_continue == 'play':
            tentativas = 1
            escolha = choice(lista)
            alternativa = []
            esc1 = list(escolha)
            escolhas_feitas = set()  
            createLine()        
            ask = False
        else: 
            ask = True

    while tentativas < 9:
        imprime()
        letra = input('Input a letter: ')
        if check_ent() != True:
            print(check_ent())
            continue

        for y in range(len(escolha)):
            if letra == esc1[y]:
                alternativa[y] = letra
                escolhas_feitas.add(letra)


        if letra not in escolha:
            print('No such letter in the word')
            tentativas += 1
            escolhas_feitas.add(letra)
        elif '-' not in alternativa and tentativas < 9:
            tentativas = 9
            print(f'You guessed the word {escolha}!')
            print('You survived!') 

    if tentativas >= 9 and '-' in alternativa:
        print('You are hanged!')