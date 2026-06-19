try:
  age=int(input('Enter age:'))
  print('age', age)
except:
    print('Enter a valid number')

try:
    number=int(input('Enter a number:'))
    result=10/number
    print(result)
except ValueError:
    print('Invalid number entered.')
except ZeroDivisionError:
    print('Cannot divide by zero.')

    