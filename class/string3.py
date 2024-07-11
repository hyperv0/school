#WAP to input two strings, if string 1 contains string 2 then create a third string with first four characters of string 2 added with word 'restore'

string1 = input("String 1: ")
string2 = input("String 2: ")

if string1 in string2:
    string3 = string2[0:5] + "restore"
    print(string3)
            