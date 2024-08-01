l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

'''
a = l[::4]
print(a)
print(l[5:15:2])
'''
slc1 = l[5:15:2]
slc2 = l[::4]
sum = avg = 0

for a in slc2:
    sum += a
    print(a, end=' ')
print()
print(f"The sum of elements in slc2 is: {sum}")

avg = sum / len(slc2)
print(f"The average of sum is: {avg}")
