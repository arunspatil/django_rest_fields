import re


def validate_string(name):
    regex = r"[a-zA-Z]+"
    match = re.match(regex, name)
    print(match)
    return match
