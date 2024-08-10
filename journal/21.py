#WAP that displays options for inserting or deleting element in the list. if the user chooses a deleting option diplay submenu and ask if element is to be deleted with value or by using its position or list slice is to be deleted. 

val = [17,23,19,19]
print('The original list', val)


while True:
    print('Main Menu')
    print('1. Insert')
    print('2. Delete')
    print('3. Exit')
    ch = int(input("Your Choice:  "))
    if ch == 1:
        item = int(input("Enter The item: "))
        pos = int(input("Enter the postion: "))
        index = pos - 1
        val.insert(index, item)
        print(val)
    elif ch == 2:
         print('1. Delete using value')
         print('2. Delete using index')
         print('3. Delete a sublist')
         dch = int(input("Your Choice:  "))
         if dch == 1:
            item = int(input("Enter The value: "))
            val.remove(item)
            print('Now the list is', val)
         elif dch == 2:
            index = int(input("Enter the index no: "))
            val.pop(index)
            print('Now the list is', val)
         elif dch == 3:
            l = int(input("Enter the lower limit: "))
            h = int(input("Enter the higher limit: "))
            del val[l:h]
            print('Now the list is', val)
    elif ch == 3:
        break
    else:
        print('Valid choice only 1, 2 and 3')
        