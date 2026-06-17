from distro import name


print('Hello World')
print('My Name Is Dominic')

# variables
name='Dominic'
age=17
student=False
x=5*5
print(name)
print(age)
print(student)
print(x)


#Data Types
#1.Integer
x=12
print(x)
#2.String
city='Mombasa'
print(city)
#3.Float
weight=23.5
print(weight)
#4.Boolean
is_boy=True
print(is_boy)

#Arithmetic Operations
b=6
y=4
print(b+y)
print(b-y)
print(b*y)
print(b/y)

#Comparison Operation
age1=20
age2=23
print(age1 == age2)
print(age1 != age2)
print(age1>age2)
print(age1<age2)
print(age1>=age2)
print(age1<=age2)

#Logical Operations
score=50
score1=65
print(score==score1 or score !=score1)
print(not(score==score1 and score !=score1))

#user input
first_name=input('Enter your first name: ')
print(first_name)
num1=float(input('Enter first number '))
num2=float(input('Enter second number '))
total=num1+num2
print(total)