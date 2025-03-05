# Remove trailing whitespaces from a string
# "string    with   spaces  " => "string with spaces "

def remove_trailing_whitespaces(text: str) -> str:
    trailing = False
    res = ''
    for ch in text:
        if ch == ' ':
            if trailing:
                continue

            trailing = True
            res += ch
        else:
            trailing = False
            res += ch

    return res