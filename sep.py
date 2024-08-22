#WAP that input a list, replicates it twice and then prints the sorted list in ascending order 

lst = eval(input('Enter the list: '))

lst2 = sorted(lst)
lst3 = sorted(lst, reversed='True')
 
print(lst2)
print(lst3)