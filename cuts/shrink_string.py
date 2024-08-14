# The task is to write a method that takes a string like
# 'aaaabbbccd' and returns a string like 'a4b3c2d'.
# The method should throw an error on non-alphabetic characters.

def stringShrink(text: str) -> str:
    if len(text) < 1:
        return ""
    
    start_char = text[0]
    counter = 0
    dupes = []
    for ch in text:
        if not ch.isalpha():
            raise Exception
        
        if ch == start_char:
            counter += 1
            continue

        dupes.append((start_char, counter))
        start_char = ch
        counter = 1

    dupes.append((start_char, counter))
    return ''.join([f'{dupe[0]}{dupe[1] if dupe[1] > 1 else ''}' for dupe in dupes])
