# Set operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Symmetric Difference:", A ^ B)

# Output:
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# Difference A-B: {1, 2}
# Symmetric Difference: {1, 2, 5, 6}