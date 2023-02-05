import os
from programs.canmaketri import canmaketri
from programs.gettable import gettable
from programs.getchartype import getchartype
from programs.getdisc import getdisc
from programs.primeornot import primeornot

def exitconfo():
    back = input('Input B to go back to menu or Q to quit (If any other input is detected, you will have to try again)')
    if back == 'Q':
        quit()

    elif back == 'B':
        os.system('cls')
        menu()
    
    else:
        exitconfo()

def menu():

    option = input('''Welcome to super IT solutions
    Choose a service from below (enter their no.)
    Input Q to quit
    [1] Discount calculator
    [2] Get type of character entered
    [3] Can 3 angles make a triangle
    [4] Print the table of any number
    [5] Check if a number is prime or not
    Your option: ''')
    os.system('cls')

    if option == 'Q':
        quit()

    try:
        option = int(option)
    
    except:
        new_input = input('''You have entered a number outside of the list or a letter/special character.
        Would you like to try again (Y/n)? (anything other than Y,x will be considered as Y) : ''')
        if new_input == 'n':
            quit()
        else:
            os.system('cls')
            menu()


    if option == 1:
        os.system('cls')
        value = input('''If your purchase value is above 10000 : 50% discount
        If your purchase value is above 5000: 30% discount
        If your purchase value is above 3000: 20% discount
        If your purchase value is 3000 or below: No discount
        Your purchase value: ''')

        print(getdisc(value))
        
        exitconfo()

    elif option == 2:
        char = input('Enter a character to be checked: ')

        try:   
            print(getchartype(char))
        except:
            char = input('You had multiple characters, please try again: ')
            getchartype(char)

        exitconfo()

    elif option == 3:
            
        canmaketri()

        exitconfo()
    
    elif option == 4:

        no = input("Which number's table do you want to generate?: ")
        
        try:
            gettable(no)
        except:
            no = input('You had entered a letter or a special character, please try again: ')
            gettable(no)

        exitconfo()
    
    elif option == 5:
        
        try:
            no = int(input('Please enter a number to be checked: '))
            primeornot(no)
        except:
            no = int(input('You had entered a letter or a special character, please try again: '))
            primeornot(no)
        exitconfo()

    else:
        
        print('You had entered a number outside of the list, please try again: ')
        menu()

menu()

#Made by Aarush