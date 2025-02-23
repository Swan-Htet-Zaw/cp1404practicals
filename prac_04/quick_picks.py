import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Generate random Quick Pick lottery numbers."""
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    """Generate a sorted list of 6 unique random numbers."""
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    return quick_pick

main()
