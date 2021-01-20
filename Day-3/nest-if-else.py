print('Hello World')

height = int(input('What is your height in cm ? '))

if height > 20:
    print('You can ride the here')
    age = int(input('What is your age ?'))
    if(age <= 12):
        print('Please pay me $5')
    elif(age <= 18):
        print('Please send me $7')
    else:
        print('Please send me $12')
else:
    print('Sorry you do not ')
