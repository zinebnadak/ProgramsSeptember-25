# Function normalize that takes a string and returns a version of the string where all characters that are not letters are removed, and all letters are converted to lowercase.
def normalize(text: str) -> str:
    return ''.join(char.lower() for char in text if char.isalpha() or char == " " )

#char.lower()               Convert each character to lowercase
#for char in text           Go through each character in the input string
#if char.isalpha() or char == " "  Keep only if it's an alphabetical letter and comprehension keeps spaces as actual characters
# "".join ()                   Joins all charachters into one single string



#Function takes a full name as input and returns the person's initials. Each initial is an uppercase letter followed by a period. Exceptions: "af", "av", "de", and "von" should be abbreviated with lowercase letters
exceptions = {"af", "av", "de", "von"}

def extract_initials(name: str) -> str:
    parts = name.strip().split()
    initials = []

    for part in parts:
        if part.lower() in exceptions:
            initials.append(part.lower()[0] + ".")
        else:
            initials.append(part.capitalize()[0] + ".")

    return "".join(initials)


# Function Checks if a password is sufficiently secure. The default parameter values mean that a password must be at least 8 characters long, contain both uppercase and lowercase letters (i.e., mixed case), and also include punctuation characters.
def check_password(password: str,
                   length: int = 8,
                   mixed_case: bool = True,
                   punctuation: bool = True) -> bool:

    if len(password) < length:
        return False

    if mixed_case:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        if not (has_upper and has_lower):
            return False

    if punctuation:
        if not any(c in string.punctuation for c in password):
            return False

    return True