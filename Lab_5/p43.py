filename = './test.txt'
with open(filename, 'a') as file:
    file.write("Tinu in!\n")

with open(filename, 'r') as file:
    print(file.read())
