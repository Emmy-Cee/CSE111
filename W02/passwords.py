import datetime
def main():
    while True:
        min_length = 10
        strong_length = 16
        word = input("Enter a password to check (or 'q' to quit): ")
        if word.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(word, min_length, strong_length)
        print(f"Password strength (0-5): {strength}\n")
        log_password_attempt(word, strength)

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"]

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
    """Check if word contains any character from character_list."""
    for char in character_list:
        if char in word:
            return True
    return False

def word_complexity(word):
    """Calculate complexity score based on character types."""
    score = 0
    if word_has_character(word, lower):
        score += 1
    if word_has_character(word, upper):
        score += 1
    if word_has_character(word, digits):
        score += 1
    if word_has_character(word, special):
        score += 1
    return score

def password_strength(word, min_length, strong_length):
    """Evaluate password strength on a scale of 0-5."""
    if word_in_file(word, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(word, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(word) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(word) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(word)
    strength = 1 + complexity
    print(f"Password complexity score: {complexity}. Strength: {strength}.")
    return strength

# This function saves a record of each password check to a file.
# It does NOT save the actual password, only the time, how long the password was, and the strength score.
def log_password_attempt(word, strength):
    """
    Log password attempt with timestamp, password length, and strength (not the actual password).
    This helps you see when you checked passwords and how strong they were.
    """
    with open("history.txt", "a", encoding="utf-8") as log_file:
        # Get the current date and time as a string
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Write the log entry to the file
        log_file.write(f"{timestamp} | word: {word} | Length: {len(word)} | Strength: {strength}\n")

if __name__ == "__main__":
    main()