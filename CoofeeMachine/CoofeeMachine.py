# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZAzQL2riNc4Q72XLwWEKrEHS6HDLSP-j
"""

class CoofeeMachine:
    money_quant = 550
    water_quant = 400
    milk_quant = 540
    coofee_quant = 120
    cups_quant = 9
    loop = True 

    def expresso():
        if CoofeeMachine.water_quant < 250:
            print('Sorry, not enough water!')
        elif CoofeeMachine.coofee_quant < 16:
            print('Sorry, not enough coofee!')
        else: 
            CoofeeMachine.money_quant += 4
            CoofeeMachine.water_quant -= 250
            CoofeeMachine.coofee_quant -= 16
            CoofeeMachine.cups_quant -= 1
            print('I have enough resources, making you a coffee!')

    def latte():
        if CoofeeMachine.water_quant < 350:
            print('Sorry, not enough water!')
        elif CoofeeMachine.milk_quant < 75:
            print('Sorry, not enough milk!')
        elif CoofeeMachine.coofee_quant < 20:
            print('Sorry, not enough coofee!')
        else: 
            CoofeeMachine.money_quant += 7
            CoofeeMachine.water_quant -= 350
            CoofeeMachine.milk_quant -= 75
            CoofeeMachine.coofee_quant -= 20
            CoofeeMachine.cups_quant -= 1
            print('I have enough resources, making you a coffee!')    

    def cappuccino():
        if CoofeeMachine.water_quant < 200:
            print('Sorry, not enough water!')
        elif CoofeeMachine.milk_quant < 100:
            print('Sorry, not enough milk!')
        elif CoofeeMachine.coofee_quant < 12:
            print('Sorry, not enough coofee!')
        else: 
            CoofeeMachine.money_quant += 6
            CoofeeMachine.water_quant -= 200
            CoofeeMachine.milk_quant -= 100
            CoofeeMachine.coofee_quant -= 12
            CoofeeMachine.cups_quant -= 1
            print('I have enough resources, making you a coffee!')

    def result():
        print('The coffee machine has:')
        print(f'{CoofeeMachine.water_quant} of water')
        print(f'{CoofeeMachine.milk_quant} of milk')
        print(f'{CoofeeMachine.coofee_quant} of coffee beans')
        print(f'{CoofeeMachine.cups_quant} of disposable cups')
        print(f'{CoofeeMachine.money_quant} of money')            

    def int_input():
        name = int(input())
        return name
    
    def str_input():
        name = input()
        name_l = name.lower()
        return name_l
   
    while loop == True:    
        print('Write action (buy, fill, take, remaining, exit):')
        select = str_input()
        if select == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
            select_type = str_input()
            if select_type == '1':
                expresso()
            elif select_type == '2':
                latte()
            elif select_type == '3':
                cappuccino()
            elif select == 'back':
                break

        elif select == 'fill':
            print('Write how many ml of water do you want to add:')
            water_add = int_input()
            CoofeeMachine.water_quant += water_add
            print('Write how many ml of milk do you want to add:')
            milk_add = int_input()
            CoofeeMachine.milk_quant += milk_add
            print('Write how many grams of coffee beans do you want to add:')
            coofee_add = int_input()
            CoofeeMachine.coofee_quant += coofee_add
            print('Write how many disposable cups of coffee do you want to add:')
            cups_add = int_input()
            CoofeeMachine.cups_quant += cups_add

        elif select == 'take':
            print(f'I gave you ${money_quant}')
            CoofeeMachine.money_quant = 0

        elif select == 'remaining':
            result()

        elif select == 'exit':
            CoofeeMachine.loop = False  
            break

"""# New Section"""