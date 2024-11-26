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
    name = input('Enter the product name: ')
    price = eval(input('Enter the product price: '))
    dict[name] = price
    ch = input('Do you want to add more records? ')

print(dict)
prod_name = input('Enter the product to be searched: ')

for i in dict:
    if i == prod_name:
        print('product found', i, 'with price as', dict[i])
