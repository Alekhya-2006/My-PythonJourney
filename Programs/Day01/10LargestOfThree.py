num1 = float(input("Enter first number: "))   
num2 = float(input("Enter second number: "))  
num3 = float(input("Enter third number: "))   

# Comparing three numbers using if-elif-else
if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)

else:
    print("Largest number is:", num3)

# Sample Output:
# Enter first number: 90
# Enter second number: 87
# Enter third number: 400
# Largest number is: 400.0