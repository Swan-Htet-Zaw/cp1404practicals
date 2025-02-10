def main():
    MIN_LENGTH = 8
    user_password = get_password(MIN_LENGTH)
    print_asterisks(user_password)

def get_password(min_length=8):
    """Prompts the user for a password and checks its minimum length."""
    while True:
        password = input(f"Enter a password (minimum {min_length} characters): ")
        if len(password) >= min_length:
            return password
        print("Error: Password too short. Try again.")

def print_asterisks(password):
    """Prints asterisks equal to the length of the given password."""
    print("*" * len(password))

main()
