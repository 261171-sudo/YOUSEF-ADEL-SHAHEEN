MAX_FAILED_ATTEMPTS = 5

role = input ("Role:")
mfa_input = input ("MFA passed (yes/no):")
failed =int(input ("Failed attempts:"))

mfa_ok = mfa_input == "yes"
is_admin = role == "admin"
can_log_in = mfa_ok and failed < MAX_FAILED_ATTEMPTS

print (f"MFA OK: {mfa_ok} ")
print(f"Privileged role : {is_admin} ")
print(f"Can log in: {can_log_in} ")