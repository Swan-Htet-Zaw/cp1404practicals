# Question 1: Ask user for their name and write it to name.txt
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Question 2: Read name from name.txt and print greeting
with open("name.txt", "r") as file:
    stored_name = file.read().strip()
print(f"Hi {stored_name}!")

# Question 3: Read the first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
print(first_number + second_number)

# Question 4: Read all numbers from numbers.txt and print their total sum
with open("numbers.txt", "r") as file:
    total = sum(int(line.strip()) for line in file)
print(total)
