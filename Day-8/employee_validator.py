# Employee Registration Validator

import re

#validation functions

def check_emp_id(emp_id):
    # should be EMP + 3 digits like EMP001
    pattern = r"^EMP\d{3}$"
    if re.match(pattern, emp_id):
        return True, "Valid"
    return False, "Format should be EMP001"


def check_name(name):
    # only letters and spaces, atleast 2 chars
    pattern = r"^[A-Za-z ]{2,}$"
    if re.match(pattern, name):
        return True, "Valid"
    return False, "Only letters allowed, min 2 characters"


def check_email(email):
    # basic email pattern 
    pattern = r"^[\w\.-]+@gmail\.com$"
    if email.endswith("@gmail.com")and re.match(pattern,email):
         return True, "Valid"
    return False, "Only Gmail addresses are allowed (example: name@gmail.com)"
    


def check_phone(phone):
    # 10 digits, starts with 6 7 8 or 9 (indian numbers)
    pattern = r"^[6-9]\d{9}$"
    if re.match(pattern, phone):
        return True, "Valid"
    return False, "Must be 10 digits starting with 6/7/8/9"


def check_password(pwd):
    # checking each condition separately and collecting errors
    errors = []

    if len(pwd) < 8:
        errors.append("min 8 characters")

    if not re.search(r"[A-Z]", pwd):
        errors.append("one uppercase letter")

    if not re.search(r"[a-z]", pwd):
        errors.append("one lowercase letter")

    if not re.search(r"\d", pwd):
        errors.append("one number")

    if not re.search(r"[!@#$%^&*]", pwd):
        errors.append("one special character (!@#$%^&*)")

    if not errors:
        return True, "Strong password"
    return False, "Password needs: " + ", ".join(errors)


print("=== Employee Registration ===")
print()

emp_id = input("Employee ID (eg. EMP001): ").strip()
name   = input("Full Name: ").strip()
email  = input("Email: ").strip()
phone  = input("Phone: ").strip()
pwd    = input("Password: ").strip()

print()
print("--- Validation ---")


results = [
    ("Employee ID", check_emp_id(emp_id)),
    ("Name",        check_name(name)),
    ("Email",       check_email(email)),
    ("Phone",       check_phone(phone)),
    ("Password",    check_password(pwd)),
]

all_ok = True

for label, (status, msg) in results:
    if status:
        print(f"  [OK]   {label} - {msg}")
    else:
        print(f"  [FAIL] {label} - {msg}")
        all_ok = False

print()
if all_ok:
    print("Registration Successful! Welcome,", name)
else:
    print("Registration Failed. Fix the errors above and try again.")
