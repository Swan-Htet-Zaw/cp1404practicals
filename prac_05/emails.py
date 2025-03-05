"""
Emails
Estimate: 25 minutes
Actual:   35 minutes
"""

def extract_name_from_email(email):
    """Extract a likely name from the email address."""
    name_part = email.split("@")[0]
    name_parts = name_part.split(".")
    name = " ".join(name_parts).title()
    return name


def main():
    """Store users' emails and names in a dictionary."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        extracted_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

        if confirmation and confirmation != "y":
            extracted_name = input("Name: ").strip().title()

        email_to_name[email] = extracted_name
        email = input("Email: ").strip()

    print("\nStored email and name data:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()
