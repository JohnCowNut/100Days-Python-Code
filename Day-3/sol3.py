year = int(input('Type year make checked Leap ? : '))

if (year % 4 == 0) and (year % 100 != 0):
    print('This year is leap')
elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print('This year is leap')
else:
    print('Not leap')


# Check count =1 or
