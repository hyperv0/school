mySubject = "Computer Science"

print(mySubject[0:len(mySubject)])
print(mySubject[-7:-1])
print(mySubject[::2])
print(mySubject[len(mySubject) - 1])
print(2*mySubject)
print(mySubject[::-2])
print(mySubject[:3] + mySubject[3:])
print(mySubject.swapcase())
print(mySubject.startswith('Comp'))
print(mySubject.isalpha())

print('--------------------------------------------')
print()


myAddress = "WZ-1,New Ganga Nagar,New Delhi"
print(myAddress.lower())
print(myAddress.upper())
print(myAddress.count('New'))
print(myAddress.find('New'))
print(myAddress.rfind('New'))
print(myAddress.split(','))
print(myAddress.split(' '))
print(myAddress.replace('New', 'Old'))
print(myAddress.partition(','))
print(myAddress.index('Delhi'))
