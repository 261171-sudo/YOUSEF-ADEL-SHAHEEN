# Simple password verification functions

def long_enough(password, minimum=8):
    """Checks if password meets the minimum length."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Ensures password is not the same as username."""
    return password != username


def password_ok(password, username):
    """Runs all checks to see if password is valid."""
    return long_enough(password) and differs_from_username(password, username)


# Main check
user = input("Username: ")
pwd = input("Password: ")

if password_ok(pwd, user):
    print("Password accepted.")
else:
    print("Password rejected.")