import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
A- smallest possible:5, largest possible:20

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
A- smallest possible:3, largest possible:9. Line 2 can't produce a 4 because the step value 2 skips even number.

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
A- smallest possible:2.5, largest possible:5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
A- print(random.randint(1, 100))
"""