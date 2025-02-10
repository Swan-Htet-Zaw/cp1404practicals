FACTOR_C_TO_F = 9.0 / 5
FACTOR_F_TO_C = 5.0 / 9
OFFSET = 32
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * FACTOR_C_TO_F + OFFSET
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = FACTOR_F_TO_C * (fahrenheit - OFFSET)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")

    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
