"""
CP1404 Practical
Emails - Program to store email and names in a dictionary

Estimated time: 25 mins
Actual time: 40 minutes
"""


def main():
    """To create a dictionary storing email and names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        validate = input(f"Is your name {name}? (Y/n)").upper()
        if validate != "Y" and validate != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """To extract name from the user email address."""
    prefix = email.split('@')
    parts = prefix[0].split('.')
    name = " ".join(parts).title()
    return name


main()
