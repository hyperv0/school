#A tuple stores (11,12,31,42, 51) where the second last element mistyped. Write the program to correct the second element as 41.

t1 = (11,12,31,42,51)
t1 = list(t1)
t1[-2] = 41
t1 = tuple(t1)
print(t1)



#write a program to input 4 elements tuple and unpack it to four variables 

t = eval(input('Input four elements: '))

a1,a2,a3,a4 = t

print(a1)
print(a2)
print(a3)
print(a4)


#WAP to input a tuple and check if it contains the all elements as same.

t = eval(input('Input elements: '))

for i in range(len(t)):
    if t[i] == t[::-1]:
        print('All the elements are same.')




#wap to print index of the minimum element in tuple

t1 = (11,12,31,42,51)
print(t1.index(min(t1)))



#wap to input a list lst and two numbers M&N.Then create a list from those 1st elements which are divisible by both M&N


M = int(input('Enter the number: '))
N = int(input('Enter the number: ' ))

lst = list(eval(input('Input list: ')))
print(lst)

lst2=[]

for i in lst:
    if i%M == 0 and i%N == 0:
        lst2.append(i)

print("elements which are divisible by both M&N are: ",lst2)


