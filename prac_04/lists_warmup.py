numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]  -> 3
numbers[-1] -> 2
numbers[3]  -> 1
numbers[:-1] -> [3, 1, 4, 1, 5, 9]  (all except the last element)
numbers[3:4] -> [1] (slice from index 3 up to (but not including) 4)
5 in numbers -> True (5 is in the list)
7 in numbers -> False (7 is not in the list)
"3" in numbers -> False ("3" is a string, but the list contains an integer 3)
numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (concatenation of lists)
"""


numbers[0] = "ten"
numbers[-1] = 1

print(numbers[2:])

print(9 in numbers)
