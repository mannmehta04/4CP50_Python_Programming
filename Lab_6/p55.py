import re

string = "Mann scored 23, Kalp scored 25, Ayush scored 24"

pattern = r"(\w+) scored (\d+)"

matches = re.findall(pattern, string)
    
for match in matches:
    name = match[0]
    marks = match[1]
    print(f"Name: {name}, Marks: {marks}")