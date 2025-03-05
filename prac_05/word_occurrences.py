"""
Word Occurrences
Estimate: 20 minutes
Actual:   23 minutes
"""

text = input("Text: ")

words = text.split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

max_word_length = max(len(word) for word in word_counts)

for word in sorted(word_counts):
    print(f"{word:{max_word_length}} : {word_counts[word]}")
