import re

invalid_sequences = ["..", ".-", "._", ".+", "+.", "++", "+-", "+_", "--", "-.", "-_", "-+", "_.", "_-", "_+", "__"]

def validate_email(email: str) -> str:
    """
    Validate an email address.

    Returns a string message explaining the result.
    """
    if not email:
        return 'email cannot be empty.'

    # basic '@' check
    if "@" not in email:
        return "Missing '@' symbol."
    if email.count("@") > 1:
        return "email contains more than one '@' symbol."

    Username, _, domain = email.partition("@")

    # Username part basic checks
    if not Username:
        return "Missing Username part (before '@')."

    if Username.startswith((".", "+", "-", "_")) or Username.endswith((".", "+", "-", "_")):
        return "Username part cannot start or end with special character."

    if any(seq in Username for seq in invalid_sequences):
        return "Multiple special characters consecutively not allowed."

    # allowed chars for Username part
    if not re.fullmatch(r"[A-Za-z0-9._+-]+", Username):
        return "Username part contains invalid characters."

    # domain basic checks
    if not domain:
        return "Missing domain part (after '@')."

    if domain.startswith((".", "+", "-", "_")) or domain.endswith((".", "+", "-", "_")):
        return "Domain cannot start or end with a special character (., +, -, _)."

    if any(seq in domain for seq in invalid_sequences):
        return "Domain can't contains multiple special characters consecutively."

    # domain must end with .TLD of 2+ letters
    if not re.fullmatch(r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", domain):
        return "Domain format is invalid (needs a valid TLD)."

    # final pattern to catch remaining edge cases
    full_pattern = (
        r"^(?!\.)"  # not start with dot
        r"[A-Za-z0-9._+\-]+"  # Username allowed chars
        r"(?<!\.)"  # not end with dot
        r"@"
        r"(?!-)"  # domain label cannot start with hyphen
        r"[A-Za-z0-9.-]+"  # domain allowed chars
        r"(?<!-)"  # domain label cannot end with hyphen
        r"\.[A-Za-z]{2,}$"  # TLD
    )
    if not re.match(full_pattern, email):
        return "email fails the final structural check."

    return "email looks valid."

while True:
    email = input("Enter an email (or 'q' to quit): ").strip().lower()
    if email == "q":
        break
    print(validate_email(email))