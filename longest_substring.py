#WAP that reads a string and displays the longest substring of the given string

str1 = input('Enter a string: ')
word = str1.split()
maxlength = 0
maxword = ''

for i in word:
    x = len(i)
    if x > maxlength and i.isalpha() == True:
        print(i)
        maxlength = x
        maxword = i

print('Substring with maxnum:', maxword)