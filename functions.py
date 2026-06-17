

def welcome():
    print('welcome home')
    print('you are welcomed')
    print('feel at home')

welcome()

def greet(name):
    print( f'Hi {name}, Please Login')
greet('Sport')
greet('Dominic')

def sum(num1,num2):
    return num1+num2
print(sum(10,23))
print(sum(100,5))

def calculate_area(length,width):
    area=length*width
    return area
print(calculate_area(5,10))




def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi
weight=float(input('Enter your weight in kg: '))
height=float(input('Enter your height in meters: '))
bmi_value=calculate_bmi(weight,height)
print(bmi_value)
if bmi_value < 18.5:
    print(' You are Underweight')
elif 18.5 <= bmi_value <= 24.9:
    print(' You are Of Normal weight')
elif 25 <= bmi_value <= 29.9:
    print(' You are Overweight')
elif bmi_value >= 30:
    print(' You are Obese')
