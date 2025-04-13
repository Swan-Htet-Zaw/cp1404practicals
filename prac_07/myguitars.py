from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main function to manage guitars."""
    guitars = load_guitars(FILENAME)

    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}.")


def load_guitars(filename):
    """Load guitars from a CSV file into a list."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name.strip(), int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars(guitars):
    """Prompt user to add new guitars to the list."""
    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    """Save the list of guitars to the CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
