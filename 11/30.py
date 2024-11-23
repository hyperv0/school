'''
#WAP to accept and store employee name as a key and his salary, allowance and deduction as value in a dictionary(dict) for 10 employees.
Display the following items:-

a. Display total salary
b. Display total allowance and deductions
c. Search an Employee
- When user selects option 1, diplay a report having Name,Salary, allowance , deduction, gross salary (salary + allowance) and net salary(gross - deductions)
- When user selects option 2, find total allowance and deductions of all 10 employees.
- When user selects option 3, accept name of the employee and search in the dictionary.
'''

D = {}
for a in range(5):
    name = input('Enter the name: ')
    salary = float(input('Enter the salary: '))
    allowance = float(input('Enter allowance: '))
    deduction = float(input('Enter deduction: '))
    D[name] = [salary,allowance,deduction]
ch = 0
while True:
    print('''
    1. Display the total salary
    2. Display total allowance and deduction
    3. Search an Employee
    ''')




