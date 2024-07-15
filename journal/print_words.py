#WAP that input a line of text and print it's each word in seperate line and also print the number of words.
s = input('Enter the line :  ')
count = 0

for word in s.split():
    print(word)
    count += 1
print('Total no. of words: ', count)
