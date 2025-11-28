a = (1, 6, 8, 4, 0, True, "Teena" )
print(type(a))
# Output: <class 'tuple'>

# Tuple Methods:
# count() : Returns the number of times a specified value in the tuple
print(a.count(8)) # 1 time

# index() : Returns the index of the first occurance of a specified value in the tuple. Raises a valueerror if the  value is not found.
print(a.index("Teena")) # Output: 6 (Index 6)

# len() : To know the length of the tuple
print(len(a)) # 7