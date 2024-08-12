#WAP to find frequences of all elements of a list. Print the list of unique elements in the list and duplicate elements in the given list.
input_list = [1,2,2,3,4,4,5,6,6,7,8,8]
frequency = {}
unique_elements = []
duplicate_elements = []

for element in input_list:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

for element in frequency:
    if frequency[element] == 1:
        unique_elements.append(element)
    else:
        duplicate_elements.append(element)

print(frequency)
print(unique_elements)
print(duplicate_elements)
