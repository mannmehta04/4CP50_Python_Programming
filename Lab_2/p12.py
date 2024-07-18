number = 5

if number == 0:
    result = 1
else:
    result = 1
    for i in range(1, number + 1):
        result *= i

print(f"The factorial of {number} is: {result}")