#WAP that takes sentence a an input where each word in a sentence seperated by a space the function should replace each blank with a hypen and then print the sentence

def main():
    a = input('Enter the sentence: ')
    print(replace(a))

def replace(x: str):
    return x.replace(" ", '-')

main()