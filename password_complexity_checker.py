import re  # Import the regular expression module

def assess_password_strength(password):
    # Get the length of the password
    length = len(password)

    # Check if the password contains at least one uppercase letter
    has_uppercase = any(char.isupper() for char in password)

    # Check if the password contains at least one lowercase letter
    has_lowercase = any(char.islower() for char in password)

    # Check if the password contains at least one digit (number)
    has_digit = any(char.isdigit() for char in password)

    # Check if the password contains at least one special character
    # (using a regular expression to match special characters)
    has_special = bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess the strength of the password based on criteria
    if length >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_uppercase or has_lowercase) and (has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"

def main():
    # Prompt the user to enter a password
    password = input("Enter your password: ")

    # Assess the strength of the password
    strength = assess_password_strength(password)

    # Print the strength assessment of the password
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
