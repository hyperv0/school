#WAP that inputs a string that contains a decimal number and prints out the decimal part of the number. If "515.8059" is given then program should 8059

number = input('Enter the number :  ')
t = number.partition('.')
print('After the partition', t)
