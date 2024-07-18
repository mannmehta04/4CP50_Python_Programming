decimal = 12

binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal //= 2

print(f"The binary representation of {decimal} is: {binary}")