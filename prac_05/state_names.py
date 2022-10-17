"""
CP1404/CP5632 Practical
State names in a dictionary
File has been formatted
"""

# Reformatted this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

# CODE_TO_NAME = {}


print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid Key Input")
    state_code = input("Enter short state: ").upper()

if not CODE_TO_NAME:  # To check if the dictionary is empty orn not
    print("The dictionary is empty.")
else:
    for code, name in CODE_TO_NAME.items():
        print(f"{code:3} is {name}")
