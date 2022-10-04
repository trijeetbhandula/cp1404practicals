"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: ValueError will occur when a user enters a non integer number in the numerator or denominator.
2. When will a ZeroDivisionError occur?
Ans: ZeroDivisionError occurs when the user enters 0 in the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: By adding a while loop, we can avoid the possibility of ZeroDivisionError
So that it avoids 0 as denominator and keeps asking user until they enter integer except 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
