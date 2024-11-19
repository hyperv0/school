a = {5: 'Number', 'a': 'string', (1,2): 'Tuple'}

for i in a:
    print(i, ':', a[i])
print(a.values())
print(a.keys())
print(a.items())
b = dict(s='number')
print(b)