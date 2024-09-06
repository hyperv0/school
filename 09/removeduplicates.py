l = eval(input('Enter the elements: '))
l = list(l)

print(l)
n = []

for i in l:
    if i not in n:
        n.append(i)
    
print(n)



