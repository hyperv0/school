#WAP that splits the string 

s = input('Enter the line :  ')
count = 0

for word in s.split():
    print(word)
    count += 1
print('Total no. of words: ', count)
