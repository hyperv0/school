#Program to calculate and print the sum of even and odd numbers of first n natural numbers.

n = int(input('n: '))
ctr = 1
sum_even = sum_odd = 0
while ctr <= n:
    if ctr%2 == 0:
        sum_even += ctr
    else:
        sum_odd += ctr
    ctr += 1

print('Sum of even numbers is', sum_even)
print('Sum of odd numbers is', sum_odd)
