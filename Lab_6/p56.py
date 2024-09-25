import re

file_path = 'mails.txt'

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = []

try:
    with open(file_path, 'r') as file:
        text = file.read()
        emails = re.findall(email_pattern, text)
        if emails:
            print("Extracted Email IDs:")
            for email in emails:
                print(email)
        else:
            print("No email IDs found.")
except FileNotFoundError:
    print(f"File not found: {file_path}")