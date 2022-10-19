"""
CP1404 Practical
Wimbledon - A program to display processed information regarding Wimbledon Gentlemen Singles Champions

Estimated time: 45 minutes
Actual time: 60 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """To display details regarding Wimbledon champions and countries by reading file."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_records(champion_to_count, countries)


def get_records(filename):
    """To get records from data file in a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """It creates a dictionary of champions to a set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_records(champion_to_count, countries):
    """To display champions with number of wins and countries."""
    print(f"Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    countries = sorted(countries)
    print(", ".join(countries))


main()
