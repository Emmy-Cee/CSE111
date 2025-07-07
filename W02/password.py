# ---
# Additional Creativity: Password History Logging
# Each time a password is checked, a record is saved to 'history.txt'.
# The log includes the date and time, the length of the password, and the strength score (0-5).
# This helps users and instructors see when password checks were made and how strong the passwords were,
# without ever saving the actual password for privacy and security.
# ---
# Character type list
import datetime

def main():
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(password)
        print(f"Password strength (0-5): {strength}\n")
        log_password_attempt(password, strength)
        
LOWER = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
UPPER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"
]

def word_in_file(word, filename, case_sensitive=False):
    """Check if word is in file. Case sensitivity optional."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True
    return False

def word_has_character(word, character_list):
    """Check if any character in word is in character_list."""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Return complexity score (0-4) based on character types in word."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Calculate password strength and print appropriate message."""
    # Check dictionary word (case-insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    # Check top password (case-sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    # Check length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    # Complexity
    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password complexity score: {complexity}. Strength: {strength}.")
    return strength

# This function saves a record of each password check to a file.
# It does NOT save the actual password, only the time, how long the password was, and the strength score.
def log_password_attempt(password, strength):
    """
    Log password attempt with timestamp, password length, and strength (not the actual password).
    This helps you see when you checked passwords and how strong they were.
    """
    with open("history.txt", "a", encoding="utf-8") as log_file:
        # Get the current date and time as a string
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Write the log entry to the file
        log_file.write(f"{timestamp} | Length: {len(password)} | Strength: {strength}\n")

if __name__ == "__main__":
    main()
