#WAP to calculate the factorial of a number

number = int(input('Enter the number: '))
fact = 1
a = 1

while a <= number:
    fact *= a
    a += 1
print('Factorial of the number is', fact)
