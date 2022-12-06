"""
CP1404 Practical
Tests for SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

# hummer = SilverServiceTaxi("Hummer", 100, 4)
# print(hummer)
fancy_taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
fancy_taxi.drive(18)
print(fancy_taxi)
print(f"${fancy_taxi.get_fare()}")
