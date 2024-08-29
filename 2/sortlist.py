#WAP to read a list of n integers (positive as well as negative) create two new lists one having all postive no. and another having all negative numbers  

def main():
    lst = [-1,2,-3,4,-5,6,7,-8]

    pos , neg = sep(lst)
    print(pos)
    print(neg)

def sep(list):
    postive = []
    negative = []

    for n in list:
        if n > 0:
            postive.append(n)
        else:
            negative.append(n)

    return postive, negative
    
main()
