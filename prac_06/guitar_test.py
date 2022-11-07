"""
CP1404/CP5632 Practical
Guitars Test
Estimate: 25 minutes
Actual: 22 minutes
"""

from prac_06.guitar import Guitar

guitar = Guitar('Gibson L-5 CES', 1922, 16035.40)
another_guitar = Guitar('Another Guitar', 2013, 999.99)

print(f'{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}')
print(f'{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}')
print(f'{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}')
print(f'{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}'
