"""
CP1404 Practical
Tests for Unreliable Car
"""

from prac_09.unreliable_car import UnreliableCar

reliable_car = UnreliableCar("Reliable Car", 100, 90)
unreliable_car = UnreliableCar("Unreliable Car", 100, 20)

for i in range(1, 10):
    print(f"Attempting to drive {i}km :")
    print(f"{reliable_car.name} drove {reliable_car.drive(i)}km")
    print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}km")

print(reliable_car)
print(unreliable_car)
