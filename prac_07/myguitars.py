"""
CP1404 Practical
More Guitars
"""

import csv
from prac_06.guitar import Guitar

FILENAME = "guitars.csv"

in_file = open(FILENAME, 'r', newline='')
reader = csv.reader(in_file)
guitars = []
for row in reader:
    guitar = Guitar(row[0], int(row[1]), float(row[2]))
    guitars.append(guitar)
in_file.close()
guitars.sort()
for guitar in guitars:
    print(guitar)

print("\nEnter details for new guitar: ")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    new_guitar_details = [name, year, cost]
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    out_file = open(FILENAME, 'a')
    writer = csv.writer(out_file)
    writer.writerow(new_guitar_details)
    out_file.close()
    name = input("Name: ")
