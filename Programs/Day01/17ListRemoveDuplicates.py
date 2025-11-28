# Remove duplicate values from a list

nums = [1, 2, 2, 3, 4, 4, 5]
uniqueNums = list(set(nums))  # Convert to set (unique only)

print("Original:", nums)
print("Without Duplicates:", uniqueNums)

# Output:
# Original: [1, 2, 2, 3, 4, 4, 5]
# Without Duplicates: [1, 2, 3, 4, 5]