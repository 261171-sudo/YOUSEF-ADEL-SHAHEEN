# fix_the_functions.py

# runtime error: print_header was called before definition
def print_header():
    """Prints login report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


print_header()


def lock_minutes(failed, minutes=15):
    """Calculates lock time in minutes."""
    if failed >= 3:
        total = failed * minutes
        # semantic error: was returning 0 instead of total
        return total
    return 0


def login_line(username, failed):
    """Formats a single login status line."""
    # semantic error: forgot to pass failed into lock_minutes
    m = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {m} min"


# runtime error: argument names were misplaced in the function call
print(login_line(username="sara", failed=4))
print(login_line("omar", 1))