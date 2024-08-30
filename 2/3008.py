#WAP a tuple t1 stores (11,21,31,41,52) where its last element is list type write a program correct its last value to 51 element 

t1 = (11,21,31,41,52)
t2 = list(t1)

t2[-1] = 51

t1 = tuple(t2)
print(t1==t2)
print(t1)
