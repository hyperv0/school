# WAP that reads a line, then counts how many times a substring "is" appears in the line and displays the count

str1 = input("Enter a line: ")
str2 = "is"
l = str1.split()
cnt = 0
for i in l:
    if i == str2:
        cnt += 1
print(f"Substring is appearing {cnt} times.")

# WAP that reads a string and displays the occurence of a vowel in the given string

str1 = input("Enter a line: ")
word = str1.split()
cnt = 0
for i in word:
    if i[0] in "aeiou" or i[0] in "AEIOU":
        cnt += 1
        print(i)
print("vowel words :", cnt)

