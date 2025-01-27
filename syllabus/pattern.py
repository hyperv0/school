#Program to input name and print the pattern as follows:
'''
name = 'ANAND'
A
AN
ANA
ANAND
'''
name = input('Enter the name: ')

for i in range(0, len(name)+1 ):
    print(name[0:i])
    