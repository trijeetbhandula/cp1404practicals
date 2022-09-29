"""To get a valid password"""
MINIMUM_LENGTH = 5

password = input("Enter the password: ")
while len(password) < MINIMUM_LENGTH:
    print("Does not meet minimum length.")
    password = input("Enter the password: ")
print("*" * len(password))
