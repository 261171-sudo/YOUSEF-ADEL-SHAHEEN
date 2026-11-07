# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

if len(password) < MIN_LENGTH:
    print("- Too short.")
elif password == username:
    print("- Same as the username.")

if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")