import re

def is_valid_email(email):
    # Regular expression for email validation
    regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the provided email matches the regex pattern
    if re.match(regex, email):
        return True
    else:
        return False

def is_valid_phone(phone):
    # Regular expression for phone number validation
    regex = r'^\+?[\d\s-]+$'
    
    # Check if the provided phone number matches the regex pattern
    if re.match(regex, phone):
        return True
    else:
        return False

