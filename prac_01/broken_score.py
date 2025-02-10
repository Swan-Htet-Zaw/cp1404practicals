"""
Program to determine the status of a score.
The score must be between 0 and 100 inclusive.
- 90 or more: Excellent
- 50 or more: Passable
- Below 50: Bad
- Invalid if outside 0 to 100
"""

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

score = float(input("Enter score: "))

if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score >= EXCELLENT_SCORE:
    print("Excellent")
elif score >= PASSABLE_SCORE:
    print("Passable")
else:
    print("Bad")
