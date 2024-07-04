#WAP to accept cost price and quantity of pencil from  user. Calculate & display total prize

cost = int(input("Enter the cost of one pencil:  "))
quantity = int(input("Enter the quantity of pencils:  "))

tp = cost*quantity

print("Total prize is: ",tp,"$")