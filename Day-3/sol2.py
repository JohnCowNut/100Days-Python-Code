# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmiPoint = weight / (height**2)

if(bmiPoint < 18.5):
    print("they are underweight")
elif bmiPoint < 25:
    print(' they have a normal weight')
elif bmiPoint < 30:
    print(' they are slightly overweight')
elif bmiPoint < 35:
    print('they are obese')
else:
    print('They are clinically obese.')
