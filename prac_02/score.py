import random

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    """Main function to get user input, determine score status, and generate a random score."""
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    print(f"Random score: {random_score}")
    print(determine_score_status(random_score))

def determine_score_status(score):
    """Determine the status of a given score and return the corresponding message."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

main()
