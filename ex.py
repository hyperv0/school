#WAP to input the roll no.s and marks of four students and create a dictionary from it

d = {}

for i in range(4):
    r,m = eval(input('Enter the roll no. and marks: '))
    d[r] = m

print(d)
    


