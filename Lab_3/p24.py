string = "A man, a plan, a canal: Panama"

modified_string = ''.join(char for char in string.lower() if char.isalnum())

if modified_string == modified_string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")