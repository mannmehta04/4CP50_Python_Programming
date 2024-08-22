decimal = 12
org = decimal

binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal //= 2

print(f"The binary representation of {org} is: {binary}")