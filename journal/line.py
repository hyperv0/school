#WAP that reads a line and prints its statistics like:
'''
1) Number of uppercase letters
2) Numbers of lowercase letters
3) Numbers of symbols
4) Number of alphabets 
5) Number of digits
'''

line = input('Enter the line :  ')
lowercount = 0
uppercount = 0
digitcount = 0
symcount = 0
alphacount = 0

for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
    elif a.isalpha():
        alphacount += 1
    elif a.isalnum() != True and a != ' ':
        symcount += 1

print(f'Number of Characters: {len(line)}')
print(f'Number of Alphabets: {alphacount}')
print(f'Number of uppercount: {uppercount}')
print(f'Number of lowercount: {lowercount}')
print(f'Number of digits: {digitcount}')
print(f'Number of symbols: {symcount}')
