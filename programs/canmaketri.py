def canmaketri():
    angles = input('Enter the 3 angles (put space between them)')
    angles = angles.split(' ')
    try:
        sum = int(angles[0]) + int(angles[1]) + int(angles[2])
        if sum == 180:
            print('These angles can make a triangle')
        else:
            print('These angles cannot make a triangle')
    except:
        print('You had entered a letter or a special character, please try again: ')
        canmaketri()
    
    return ' '

