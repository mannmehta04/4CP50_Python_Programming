for i in range(1, 5):
    for j in range(i, 0, -1):
        print(" " * (i - j), end="")
        if j == i:
            print(chr(97 + i), end="")
        else:
            print(chr(97 + j - 1), end="")
    print()