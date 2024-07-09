p = int(input('Principal amount: '))
r = int(input('Rate of interest: '))
time = int(input('Time in years: '))

si = (p*r*time)/100
amt = p + si 

print(amt)
