"""
Password check program
"""

# Minimum length
MIN_LENGTH = 8


def get_password(min_length):
    """Get password, checking minimum_length"""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long!")
        password = input("Enter a password: ")
    return password


def main():
    """Get and print password"""
    password = get_password(MIN_LENGTH)
    print('*' * len(password))


main()
