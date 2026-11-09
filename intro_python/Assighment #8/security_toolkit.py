# Security Toolkit Main Project

MIN_LENGTH = 8
def border(width):
    """Prints top/bottom border line."""
    print("+" + "-" * width + "+")


def show_box(text):
    """Prints text enclosed inside a text box."""
    w = len(text) + 2
    border(w)
    print(f"| {text} |")
    border(w)


def show_menu():
    """Displays user menu options."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Classifies network port numbers."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Handles port check flow."""
    val = int(input("Port: "))
    res = port_range(val)
    show_box(f"Port {val}: {res}")


def password_problem(password, username):
    """Validates password rules."""
    if len(password) < MIN_LENGTH:
        return "too short (at least 8)"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Handles password check flow."""
    u = input("Username: ")
    p = input("Password: ")
    prob = password_problem(p, u)
    
    if prob:
        show_box(f"Rejected: {prob}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Calculates brute force time in days."""
    total = 10 ** digits
    secs = total // per_second
    return secs // 86400


def check_pin():
    """Handles PIN check flow."""
    d = int(input("PIN digits: "))
    s = int(input("Guesses per second: "))
    days = days_to_guess(d, s)
    show_box(f"{d} digits: {days} days")


def main():
    """App main loop."""
    count = 0
    show_menu()
    
    while True:
        choice = input("Choice (1, 2, 3, or q): ")
        if choice == "1":
            check_port()
            count += 1
        elif choice == "2":
            check_password()
            count += 1
        elif choice == "3":
            check_pin()
            count += 1
        elif choice == "q":
            show_box(f"Checks done: {count}")
            break
        else:
            print("Unknown choice.")


if __name__ == "__main__":
    main()