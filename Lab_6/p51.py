class Person:
    def greet(self):
        return "Hello!"

class Employee:
    def work(self):
        return "Working on tasks."

class Manager(Person, Employee):
    def manage(self):
        return "Managing the team."

manager = Manager()

print(manager.greet())
print(manager.work())
print(manager.manage())