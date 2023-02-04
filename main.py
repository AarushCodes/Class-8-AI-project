import os

def getdisc(value):
    try:
        value = float(value)
        if value > 10000:
            disc = value / 2
        elif value > 5000:
            disc = value * (30/100)
        elif value > 3000:
            disc = value * (20/100)
        else:
            disc = 0
        disctprc = value - disc
        print(f'On purchase of Rs {value} you will save Rs {disc} and you will have to pay {disctprc}')
    
    except:
        value = input('You had entered a letter or a special character, please try again: ')
        getdisc(value)

    return ' '
    

def getchartype(char):
    if ord(char) >= 65 and ord(char) <= 90:
        chartype = 'Capital Letter'
    elif ord(char) >= 97 and ord(char) <= 122:
        chartype = 'Lowercase Letter'
    elif ord(char) >= 48 and ord(char) <= 57:
        chartype = 'Number'
    else:
        chartype = 'unknown'
    print(f'The character you entered is a {chartype}')
    return ' '

def canmaketri():
    angles = input('Enter the 3 angles (put space between them)')
    angles = angles.split(' ')
    try:
        sum = int(angles[0]) + int(angles[1]) + int(angles[2])
    except:
        print('You had entered a letter or a special character, please try again: ')
        canmaketri()
    
    if sum == 180:
            print('These angles can make a triangle')
    else:
         print('These angles cannot make a triangle')
        
    return ' '

def gettable(no):
    no = int(no)
    for i in range(1, 11):
        print(no, 'x', i, '=', no*i)
    return ' '

def primeornot(no):
    flag = 0
    i = 2
    while i <= (no/2):
        if (no%i) == 0:
            flag = 1
            break
        else:
            i += 1
    if no == 1:
        print('1 is neither prime nor composite')
    elif flag == 0:
        print(no,' is a prime number.')
    elif flag == 1:
        print(no,'is not a prime number.')

    return ' '


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

    option = int(input('''Welcome to super IT solutions
    Choose a service from below (enter their no.)
    Input Q to quit
    [1] Discount calculator
    [2] Get type of character entered
    [3] Can 3 angles make a triangle
    [4] Print the table of any number
    [5] Check if a number is prime or not
    Your option: '''))
    os.system('cls')

    if option == 'Q':
        quit()

    elif option == 1:
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
            no = input('You had entered a letter or a special character, please try again: ')
            primeornot(no)
        exitconfo()

    else:
        new_input = input('''You have entered a number outside of the list or a letter/special character.
Would you like to try again (Y/n)? (anything other than Y,x will be considered as Y) : ''')

        if new_input == 'n':
            quit()
        else:
            os.system('cls')
            menu()

menu()

#Made by Aarush