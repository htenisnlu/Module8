# Hikmet Tenis
# 08/17/2024
# This function function that takes two inputs from a user and 
# prints whether the sum is greater than 10, less than 10, or equal to 10.

def check_sum():
    # Get the first number from the user and convert it to an integer
    num1 = int(input("Enter the first number: "))
    
    # Get the second number from the user and convert it to an integer
    num2 = int(input("Enter the second number: "))
    
    # Calculate the sum of the two numbers
    total = num1 + num2
    
    # Check if the sum is greater than, less than, or equal to 10
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")
