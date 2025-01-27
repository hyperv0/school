#write the output of the following code

text = 'gmail@com'
l = len(text)
ntext = ''

for i in range(0, l):
    if text[i].isupper():
        ntext = ntext + text[i].lower()
    elif text[i].isalpha():
        ntext = ntext + text[i].upper()
    else:
        ntext = ntext + 'bb'
print(ntext)
