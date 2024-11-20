'''
write a menu-driven program to input names of n students, total marks,average result and store in nested tuple.
display the following menu:

a) Result: Display name, marks, average and assign result as 'pass' if avg is more than 32 and 'fail' if less than 33
b) Display:  Display name, total marks and average of all students.
d) Merit list: Display students getting average marks above 74.
'''

n = int(input('No of students: '))
tup = ()
names = []

for i in range(n):
    name = input('Enter the name: ')
    t_marks = int(input('Enter the marks: '))
    avg = float(input('Average: '))
    print()
    t = (name, t_marks, avg)
    tup += (t,)

while True:
    print('Menu')
    print('1. Accept')
    print('2. Display')
    print('3. Search')
    print('4. Merit List')
    print('5. Exit')

    ch = int(input('Enter your choice: '))
    #accept
    if ch == 1: 
        for i in tup:
            print(i[0], i[2])
        if i[2] > 32:
            print('Result is "passed".')
        else:
            print('Result is "failed".')

    #display
    elif ch == 2: 
        for i in tup:
            print(i[0], i[1], i[2])

    #search
    elif ch == 3:
        name1 = input('Name: ')
        if name1 in names:
            pos = names.index(name1)
            print(tup[pos][0], tup[pos][1])
        else:
            print('Name not found.')

    #merit list
    elif ch == 4:
        for i in tup:
            if (i[2] > 75):
                print(i[0])

    #exit
    elif ch == 5:
        break
