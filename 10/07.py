#WAP to create a dictionary containing names of competition winner students as keys and number of their wins and values

n = int(input('Enter the number of students: '))

compwinners = {}

for a in range(n):
    keys = input('Name of the student: ')
    values = input('Number of competitions won: ')
    compwinners[keys] = values
print(compwinners)
