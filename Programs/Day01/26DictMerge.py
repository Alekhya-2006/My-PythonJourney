# Merging dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2        
# merged = {**dict1, **dict2}  # Alternate

print("Merged Dictionary:", merged)

# Output 
# Merged Dictionary: {'a': 1, 'b': 3, 'c': 4}