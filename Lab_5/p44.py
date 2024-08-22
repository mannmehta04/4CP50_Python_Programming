filename = 'food.txt'
with open(filename, 'w+') as file:
    file.write("Cake\n")
    file.write("Burger\n")
    file.write("Pizza\n")

food = []
with open(filename, 'r') as file:
    food = file.readlines()

print(food)