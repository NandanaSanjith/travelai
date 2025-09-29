from email_validator import validate_email, EmailNotValidError
from datetime import date

def is_valid_email(email: str) -> bool:
    try:
        # Validate & normalize
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def get_todays_date():
    return date.today()