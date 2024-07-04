#7. Program to print a pattern of numbers, where each row contains the row number repeated 'n' times
n=int(input("Enter number of rows: "))
for i in range(n):
    print((str(i+1))*n)


'''
Ans:
Enter number of rows: 5

11111
22222
33333
44444
55555
'''