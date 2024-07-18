start = 100
end = 500

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    digits = str(num)
    length = len(digits)
    sum_of_powers = sum(int(digit) ** length for digit in digits)
    if sum_of_powers == num:
        print(num)