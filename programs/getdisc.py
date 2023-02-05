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