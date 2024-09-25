import re

pattern = r'^m..$'

strings = ["mat", "max", "mop", "mouse", "hello", "world"]

for s in strings:
    if re.match(pattern, s):
        print(f"Matching: {s}")
    else:
        print(f"Not matching: {s}")