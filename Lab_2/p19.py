n = int(input("Enter the value of n: "))

if n <= 0:
    print("Error: n must be greater than 0.")
else:
    result = 0
    for i in range(1, n+1):
        result += i / (i + 1)
    print(f"The sum of the series is: {result:.2f}")