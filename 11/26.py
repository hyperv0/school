'''
Rajmandir basket is a department store with a wide range of merchandise including groceries, fruits, vegetables and household accessories. 
It aims to develop computer software for billing, inventory and accounts management and to provide consumers a user-friendly interface to view item codes and prices of 
various items.

Write a program that repeatedly asks the user to enter product names and prices. Store all of them in a dictionary whose keys are product names and values are prices. 
Also write a code to search an item from the dictonary.
''' 

dict = {}
ch = 'Y'

while ch == 'Y' or ch == 'y':
    cust_name = input('Enter the product name: ')
    phone = eval(input('Enter the product price: '))
    dict[name] = phone
    ch = input('Do you want to add more records? ')

print(dict)
cust_name = input('Enter the customer to be searched: ')

for i in dict:
    if i == cust_name:
        print('customer found', i, 'with phone as', dict[i])
