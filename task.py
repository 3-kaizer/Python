name = input('Employee Name:')
hours_worked = float(input('Hours Worked:'))
hourly_rate = float(input('Hourly Rate:'))
tax = float(input('Tax: '))

gross_salary = hours_worked * hourly_rate
net_salary = gross_salary - tax


print('Net Salary:', net_salary)