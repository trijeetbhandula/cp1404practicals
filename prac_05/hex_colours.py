"""
CP1404 Practical
Hexadecimal Colour Dictionary
"""

COLOUR_CODES = {"Amaranth": "#e52b50", "Aqua": "#00ffff", "Blond": "#faf0be",
                "Chocolate": "#d2691e", "Fawn": "#e5aa70", "Harlequin": "#3fff00",
                "Indigo": "#4b0082", "Lavender": "#e6e6fa", "Plum": "#8e4585", "Zaffre": "#0014a8"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid Colour")
    colour_name = input("Enter colour name: ").title()
