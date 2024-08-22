filename = './test.txt'
with open(filename, 'w') as file:
    file.write("Tini in!\n")

with open(filename, 'r') as file:
    content = file.read()
    print(content)
