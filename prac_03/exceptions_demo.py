"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A- A ValueError occurs when the user enters a non-integer value for the numerator or denominator.

2. When will a ZeroDivisionError occur?
A- A ZeroDivisionError occurs when the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A- Yes, by checking if the denominator is zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a valid denominator.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")