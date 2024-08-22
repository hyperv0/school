#WAP that reads a string and check whether it is a palandrome string or not

def is_palindrome(s:str):
    return s == s[::-1]

s = input('Enter the string: ')
print('Palindrome: ',is_palindrome(s))