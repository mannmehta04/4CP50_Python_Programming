import re

def find_words_starting_with_b(text):
    pattern = r'\b(b\w*)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches

text = "Trump wants his blue blazer black"
print(find_words_starting_with_b(text))