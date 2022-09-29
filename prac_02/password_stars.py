"""To get a valid password"""

MINIMUM_LENGTH = 5


def main():
    password = get_valid_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_valid_password():
    password = input("Enter the password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Does not meet minimum length.")
        password = input("Enter the password: ")
    return password


main()
