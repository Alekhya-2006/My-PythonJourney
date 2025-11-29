# Store marks and take average

marks = {
    "Math": 95,
    "Physics": 88,
    "Chemistry": 92,
    "Biology": 85
}

total = sum(marks.values())
avg = total / len(marks)

print("Total:", total)
print("Average:", round(avg, 2)) # round to 2 decimal places

# Output:
# Total: 360
# Average: 90.0