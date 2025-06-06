def is_valid_email(email: str) -> bool:
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def format_email(email: str) -> str:
    return email.strip().lower()