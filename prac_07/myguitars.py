"""
CP1404 Practical
Guitars
"""

import csv
from prac_06.guitar import Guitar

in_file = open('guitars.csv', 'r', newline='')
reader = csv.reader(in_file)
guitars = []
for row in reader:
    guitar = Guitar(row[0], int(row[1]), float(row[2]))
    guitars.append(guitar)
in_file.close()
guitars.sort()
for guitar in guitars:
    print(guitar)
