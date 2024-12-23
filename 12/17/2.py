#WAP input a string and check if it contains a digit or not

s = input('Enter a string: ')
digitcount = 0

for i in s:
    if i.isdigit():
        digitcount += 1
    
if digitcount > 0:
    print(' The given string contains a digit.')