# Add and remove elements

fruits = {"apple", "banana"}

fruits.add("mango")         # Add element
fruits.remove("banana")     # Remove element (error if not present)
fruits.discard("grape")     # No error even if element not present

print(fruits)

# Output:
# {'apple', 'mango'}