Fruits = ["Apple", "Banana", "Guava",]
print(Fruits[0]) 

Fruits[0] = "Pomogranate" # Unlike Strings, Lists are mutable
print(Fruits[0])

print(Fruits)


# List Slicing
# List slicing can be done as strings.
print(Fruits[0:2])

'''Sample Output:
Apple
Pomogranate
['Pomogranate', 'Banana', 'Guava']
['Pomogranate', 'Banana']
'''