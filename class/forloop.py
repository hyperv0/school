'''rows = 6

for i in range(rows):
    for j in range(i):
        print(j + 1, end=" ")
    print()
'''


'''for i in range(6):
    for j in range(i):
        print(i, end=' ')
    print()
'''


'''for i in range(6):
    for j in range(i):
        print('*', end=" ")
    print()
'''

'''for i in range(6, 0 , -1):
    for j in range(i):
        print(i, end=' ')
    print()'''

'''for i in range(6, 0, -1):
    for j in range(i):
        print('*', end=" ")
    print() 
'''

'''for i in range(1, 10, 2):
    for j in range(1, i + 1, 2):
        print(i, end=" ")
    print() 
'''


u = "ABCDE"

for i in range(6):
    for j in range(i, i+1):
        print(u[i-1]*i, end=" ")
    print()


