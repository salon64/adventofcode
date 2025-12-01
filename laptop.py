import itertools

# Define the set of valid characters
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

# Define a function to check the conditions for the password
def check_conditions(password):
    # Ensure the password is exactly 16 characters
    if len(password) != 16:
        return False

    # Convert password to a list of integer values (byte values)
    s = [ord(c) for c in password]

    # Check all the conditions
    if not all(c in chars for c in password):
        return False
    if (s[5] - s[3]) < -4: return False
    if (s[11] - s[0]) == -5: return False
    if (s[4] ^ s[12]) == 2: return False
    if (s[13] ^ s[1]) == 19: return False
    if (s[10] | s[1]) == 126: return False
    if (s[7] | s[4]) == 108: return False
    if (s[15] ^ s[6]) == 16: return False
    if (s[8] ^ s[9]) == 9: return False
    if (s[2] + s[11]) == 226: return False
    if (s[14] - s[3]) == -5: return False
    if (s[8] | s[7]) == 125: return False
    if (s[3] + s[11]) < 226: return False
    if (s[5] ^ s[9]) == 8: return False
    if (s[11] | s[10]) == 111: return False
    if (s[1] ^ s[3]) == 2: return False
    if (s[12] ^ s[2]) == 25: return False
    if (s[9] ^ s[15]) == 26: return False

    return True

# Brute-force over all possible 16-character passwords
for password_tuple in itertools.product(chars, repeat=16):
    password = ''.join(password_tuple)

    if check_conditions(password):
        print("Found valid password (flag):", password)
        break
else:
    print("No valid password found.")
