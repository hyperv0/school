#WAP to input a list and two numbers M and N then create a list from those list elements which are divisible by M and N 

lst = eval(input('Enter the list: '))
lst2 = []
M, N = eval(input('Enter the two numbers M and N: '))

for num in lst:
    if (num % M == 0) and (num % N == 0):
        lst2.append(num)

print('New list', lst2)
