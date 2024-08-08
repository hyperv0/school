#WAP that displays options fro inserting or deleting element in the list. if the user chooses a deleting option diplay submenu and ask if element is to be deleted with value or by using its position or list slice is to be deleted. 

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
    elif ch == 3:
        break

