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