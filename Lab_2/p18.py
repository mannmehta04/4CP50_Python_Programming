number = 24

print(f"The factors of {number} are:", end=" ")

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=", ")