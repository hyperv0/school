ch = 0
list = []

while True:
    print("\nList Menu")
    print("1. Add a customer")
    print("2. Modify customer details")
    print("3. Delete customer details")
    print("4. Sort customer list")
    print("5. Display sorted list")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("1. Add amount deposited")
        print("2. Add a customer record")
        ch1 = int(input("Enter choice 1 or 2: "))
        if ch1 == 1:
            amt = int(input("Enter deposited amount: "))
            pos = int(input("Enter position to add: "))
            list.insert(pos, amt)
        elif ch1 == 2:
            list2 = eval(input("Enter added customer list: "))
            list.extend(list2)
        else:
            print("Valid choices are 1 or 2")
        print("Successfully added")

    elif ch == 2:
        pos = int(input("Enter position whose details are to be modified: "))
        new_cust = int(input("Enter new value: "))
        old = list[pos]
        list[pos] = new_cust
        print(old, "modified with", new_cust)

    elif ch == 3:
        print("1. Delete details by position")
        print("2. Delete details by customer number")
        ch1 = int(input("Enter your choice as 1 or 2: "))
        if ch1 == 1:
            pos = int(input("Enter position: "))
            list.pop(pos)
            print("Successfully deleted")
        elif ch1 == 2:
            cust = int(input("Enter element: "))
            list.remove(cust)
            print("Successfully deleted")
        else:
            print("Valid choices are 1 or 2")

    elif ch == 4:
        print("1. Ascending")
        print("2. Descending")
        ch1 = int(input("Enter choice 1 or 2: "))
        if ch1 == 1:
            list.sort()
        elif ch1 == 2:
            list.sort(reverse=True)
        else:
            print("Valid choices are 1 or 2")

    elif ch == 5:
        print(list)

    elif ch == 6:
        break

    else:
        print("Valid choice is 1 to 6")
