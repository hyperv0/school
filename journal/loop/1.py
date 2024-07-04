#1. Program to print number pattern

rows = int(input('Enter the number of rows: '))
# outer loop
for i in range(rows + 1):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')

'''
Ans:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''