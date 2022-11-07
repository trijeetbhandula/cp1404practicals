"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
Estimate: 30 minutes
Actual: 34 minutes
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print(my_car.name)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.name)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
