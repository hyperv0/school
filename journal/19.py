#WAP to input a list and an element, and remove all occurances of the given element from the list

lst = eval(input('Enter the list: '))
item = int(input('Enter the element: '))

c = lst.count(item)

if c == 0:
    print(item, 'not found in the list')
else:
    while c > 0:
        i = lst.index(item)
        lst.pop(i)
        c = c - 1
print('list after removing the element', lst)
