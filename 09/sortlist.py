lst = [-1,2,-3,4,-5,6,7,-8]

postive = []
negative = []

for n in lst:
    if n > 0:
        postive.append(n)
    else:
        negative.append(n)
print(postive)
print(negative)