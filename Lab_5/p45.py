data = ["Cake\n", "Burger\n", "Pizza\n"]

filename = 'foodList.txt'
with open(filename, 'w') as file:
    file.writelines(data)
