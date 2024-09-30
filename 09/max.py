l1 = eval(input('Enter the elements for list1: '))
l2 = eval(input('Enter the elements for list2: '))

maxl1 = max(l1)
maxl2 = max(l2)

if maxl1 > maxl2:
    print('maximum:',maxl1,'\nindex:',l1.index(maxl1),', from list1')
else:
    print('maximum:', maxl2,'\nindex:',l2.index(maxl2),', from list2')