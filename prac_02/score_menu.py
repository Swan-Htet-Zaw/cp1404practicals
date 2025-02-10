import random

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Main function to control the menu and handle user interactions."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_score_status(score)}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice. Please select from the menu.")

        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye! Thanks for using the program.")

def get_valid_score():
    """Prompt the user to enter a valid score (0-100 inclusive)."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if MIN_SCORE <= score <= MAX_SCORE:
                return score
            print("Invalid score! Must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def determine_score_status(score):
    """Determine the status of a given score and return the corresponding message."""
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print stars equal to the length of the given score."""
    print("*" * int(score))

main()
