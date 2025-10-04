import re

# List of common weak passwords
weak_passwords = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "letmein", "monkey", "12345678", "password1"
]

def check_password_strength(password):
    # Check if the password is in the common weak list
    if password.lower() in weak_passwords:
        return "❌ Very Weak: This password is too common!"
    
    # Check password length
    if len(password) < 8:
        return "❌ Weak: Password should be at least 8 characters long."
    
    # Check uppercase letters
    if not re.search(r"[A-Z]", password):
        return "⚠️ Medium: Add at least one uppercase letter."
    
    # Check lowercase letters
    if not re.search(r"[a-z]", password):
        return "⚠️ Medium: Add at least one lowercase letter."
    
    # Check numbers
    if not re.search(r"\d", password):
        return "⚠️ Medium: Add at least one number."
    
    # Check special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "⚠️ Strong but could be stronger: Add a special character."
    
    return "✅ Very Strong: Your password is secure!"

def main():
    print("🔒 Password Strength Checker 🔒")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_pass = input("Enter a password to check: ")
        if user_pass.lower() == "exit":
            print("Goodbye! Stay safe! 🔐")
            break
        print(check_password_strength(user_pass), "\n")

if __name__ == "__main__":
    main()import re

# List of common weak passwords
weak_passwords = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "letmein", "monkey", "12345678", "password1"
]

def check_password_strength(password):
    # Check if the password is in the common weak list
    if password.lower() in weak_passwords:
        return "❌ Very Weak: This password is too common!"
    
    # Check password length
    if len(password) < 8:
        return "❌ Weak: Password should be at least 8 characters long."
    
    # Check uppercase letters
    if not re.search(r"[A-Z]", password):
        return "⚠️ Medium: Add at least one uppercase letter."
    
    # Check lowercase letters
    if not re.search(r"[a-z]", password):
        return "⚠️ Medium: Add at least one lowercase letter."
    
    # Check numbers
    if not re.search(r"\d", password):
        return "⚠️ Medium: Add at least one number."
    
    # Check special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "⚠️ Strong but could be stronger: Add a special character."
    
    return "✅ Very Strong: Your password is secure!"

def main():
    print("🔒 Password Strength Checker 🔒")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_pass = input("Enter a password to check: ")
        if user_pass.lower() == "exit":
            print("Goodbye! Stay safe! 🔐")
            break
        print(check_password_strength(user_pass), "\n")

if __name__ == "__main__":
    main()