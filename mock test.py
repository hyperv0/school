import pickle
while True:
  print('''
        1. Add Record
        2. Display Record
        3. Search Record
        4. Exit
  ''')
  ch=int(input("Enter your choice:"))
  l=[]
  if ch==1:
    f=open("Employee.dat","ab")
    Empid=int(input("Employee ID:"))
    EName=input("Employee name:")
    dept=input("Enter department:")
    salary=float(input("Enter salary:"))
    l=[Empid,EName,dept,salary]
    pickle.dump(l,f)
    print("Record Added Successfully.")
    f.close()
  elif ch==2:
    f=open("Employee.dat","rb")
    while True:
      try:
        dt=pickle.load(f)
        print(dt)
      except EOFError:
        break
    f.close()
  elif ch==3:
    si=int(input("Enter Employee ID:"))
    f=open("Employee.dat","rb")
    fl=False
    while True:
      try:
        dt=pickle.load(f)
        for i in dt:
          if i==si:
            fl=True
            print("Record Found...")
            print("ID:",dt[0])
            print("Name:",dt[1])
            print("Brand:",dt[2])
            print("Price:",dt[3])
      except EOFError:
        break
    if fl==False:
      print("Record not found...")
    f.close()
  elif ch==4:
    break
  else:
    print("Invalid Choice")
