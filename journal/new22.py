#WAP to input 4 elements tuple and unpack it to four variable . Then recreate the tuple with element swapped as 1 st element with 3rd and 2nd with 4th element

t = eval(input('Input four elements: '))

a1,a2,a3,a4 = t

a1 = a3
a2 = a4
tup = a1,a2,a3,a4

tup = tuple(tup)

print(f'After recreation: {tup}')

print(f'length of the tuple: {len(tup)}')
print(f'Minimum value: {min(tup)}')
print(f'Maximum value: {max(tup)}')
reversed = sorted(tup, reverse=True)
print(reversed)
