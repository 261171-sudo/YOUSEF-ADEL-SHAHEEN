# Lock tools helper functions
def is_locked(failed, max_tries=3):
    """Checks if the account is locked based on failed attempts."""
    return failed >= max_tries
def tries_left(failed, max_tries=3):
    """Calculates remaining tries before locking."""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed


def status(failed):
    """Returns string representation of current account status."""
    if is_locked(failed):
        return "locked"
    
    left = tries_left(failed)
    return f"active ({left} tries left)"


# Tests
print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))