'''
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Length error (min 8 chars)': length_error,
        'Must contain a digit': digit_error,
        'Must contain an uppercase letter': uppercase_error,
        'Must contain a lowercase letter': lowercase_error,
        'Must contain a special character': symbol_error
    }

    if not any(errors.values()):
        return "Strong password ", errors
    elif sum(errors.values()) <= 2:
        return "Moderate password ", errors
    else:
        return "Weak password ", errors


# Example
password = input("Enter your password: ")
strength, details = check_password_strength(password)
print(f"\nPassword Strength: {strength}")
print("\nDetails:")
for k, v in details.items():
    print(f"{k}: {'no' if v else 'yes'}")

'''

import re

def check_password_strength(password):
    # Each condition gives 20% if passed (total 100%)
    criteria = {
        'Length >= 8': len(password) >= 8,
        'Has digit': re.search(r"\d", password) is not None,
        'Has uppercase letter': re.search(r"[A-Z]", password) is not None,
        'Has lowercase letter': re.search(r"[a-z]", password) is not None,
        'Has special character': re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    }

    passed = sum(criteria.values())
    strength_percentage = (passed / len(criteria)) * 100

    if strength_percentage == 100:
        status = "Strong"
    elif strength_percentage >= 60:
        status = "Moderate"
    else:
        status = "Weak"

    return strength_percentage, status, criteria


# Example usage
password = input("Enter your password: ")
percentage, status, checks = check_password_strength(password)

print(f"\nPassword Strength: {percentage:.0f}% - {status}")
print("\nCriteria:")
for check, passed in checks.items():
    print(f"{check}: {'yes' if passed else 'no'}")
    
