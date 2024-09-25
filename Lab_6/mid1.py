f1 = open("f1.txt", "r")
f2 = open("f2.txt", "r")
f3 = open("f3.txt", "w+")
lines1 = f1.readlines()
lines2 = f2.readlines()

max_lines = max(len(lines1), len(lines2))
0
for i in range(max_lines):
    if i < len(lines1):
        f3.write(lines1[i])
    if i < len(lines2):
        f3.write(lines2[i])