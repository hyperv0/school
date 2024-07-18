#WAP that input a string having some digits, write a program to calculate the sum of digits present in the string

s = input('Enter the string: ')
num = 0

for char in s:
    if s.isdigit():
        num += int(char)
print('Sum of digits is : ', num)