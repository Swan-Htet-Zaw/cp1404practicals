name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Using f-string formatting to produce the required output:
print(f"{year} {name} for about ${cost:,.0f}!")

# Using a for loop with the range function and f-string formatting
for i in range(11):
    print(f"2 ^ {i:2} is {2**i:4}")
