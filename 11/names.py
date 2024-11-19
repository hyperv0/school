#WAP to input 'n' names and phone number to store it in a dictionary and print the phone number of a particular name

phone = dict()
i = 1
n = int(input('Enter the number of entries: '))

while i <= n:
    a = input('Enter the name: ')
    b = input('Enter the phone no.: ')
    phone[a] = b
    i += 1

l = phone.keys()
x = input('Enter the name to be searched: ')

if x not in l:
    print(x, 'does not exist.')
else:
    for i in l:
        if i == x:
            print(f'{x}:{phone[i]}')
            