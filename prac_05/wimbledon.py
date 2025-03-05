"""
Wimbledon Champions Data Processing
Estimate: 30 minutes
Actual:   42 minutes
"""

FILENAME = "wimbledon.csv"

def read_wimbledon_data(filename):
    """Read the Wimbledon CSV file and return a list of champion data."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()[1:]  # Skip header line
    return [line.strip().split(",") for line in lines]


def process_wimbledon_data(data):
    """Process Wimbledon data to determine champion wins and unique winning countries."""
    champion_wins = {}  # Dictionary for champion win counts
    winning_countries = set()  # Set for unique winning countries

    for entry in data:
        country = entry[1]
        champion = entry[2]

        champion_wins[champion] = champion_wins.get(champion, 0) + 1
        winning_countries.add(country)

    return champion_wins, winning_countries


def display_results(champion_wins, winning_countries):
    """Display the champions with their wins and countries sorted alphabetically."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(winning_countries), "countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


def main():
    """Main function to orchestrate reading, processing, and displaying Wimbledon data."""
    data = read_wimbledon_data(FILENAME)
    champion_wins, winning_countries = process_wimbledon_data(data)
    display_results(champion_wins, winning_countries)

main()
