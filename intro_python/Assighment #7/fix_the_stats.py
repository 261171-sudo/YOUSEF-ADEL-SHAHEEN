# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1 (semantic): The counters must start at 0 before the loop, not inside it.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2 (semantic): Use / for division instead of integer division //.
# Bug 3 (semantic): Print once, after the loop (unindented).
# Bug 4 (safety check): Prevent ZeroDivisionError when count is 0.
if count > 0:
    print(f"Average session: {total / count} minutes")
else:
    print("Average session: 0 minutes")

# Bug 5 (semantic): range(1, 4) stops before 4; use range(1, 5) to print levels 1 to 4.
for level in range(1, 5):
    print(f"Level {level}")