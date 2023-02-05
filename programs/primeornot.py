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