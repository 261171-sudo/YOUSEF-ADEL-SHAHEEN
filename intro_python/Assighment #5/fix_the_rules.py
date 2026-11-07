role = input("Role: ")
port = int(input("Port: "))

is_admin = role == "admin"
is_system_port = port <= 1023
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")