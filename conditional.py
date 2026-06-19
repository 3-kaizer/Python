#conditional statements
#if...else...
age=16
if age>=18:
    print('you are an adult')
else:
    print('you are a child')


marks=102
if marks>=80 and marks<=100:
    print('Grade A')
elif marks>=70 and marks<80:
    print('Grade B')
elif marks>=60 and marks<70:
    print('Grade C')
elif marks>=50 and marks<60:
    print('Grade D')
else:
    print('Below Average')

correct_username ='Dominic'
correct_password ='0147'

username=input('Enter your username: ')
password=input('Enter your password: ')


if username==correct_username and password==correct_password:
    print('Login successful')
else:    print('Invalid credentials')

AccountBalance=float(input('Enter your Account Balance: '))
withdrawal_amount=float(input('Enter the amount you want to withdraw: '))
Balance=float(AccountBalance-withdrawal_amount)

if withdrawal_amount <= AccountBalance:
    print('Transaction successful')
    print(' Balance:', Balance)
if withdrawal_amount > AccountBalance:
     print('Transaction failed')
     print('insufficient funds')
     
    








