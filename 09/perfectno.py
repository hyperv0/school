num = int(input('Enter the number: '))
sum1 = 0

for i in  range(1,num):
    if (num % i == 0):
        sum1 = sum1 + i
if (sum1 == num):
    print('Perfect Number')
else:
    print('Not a perfect number')