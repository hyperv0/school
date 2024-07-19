#WAP that read a line and substring, it should display the number of occurances of the given substring in a line

line = input('Enter the line: ')
substring = input('Enter the substring: ')

length = len(line)
length_sub = len(substring)

start = count = 0
end = length

while True:
    pos = line.find(substring, start, end)
    if pos != -1:
        count += 1
        start = pos + length_sub
    else:
        break
    if start >= length:
        break

print('Number of occurances of substring: ', count)     

