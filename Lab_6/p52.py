class BaseClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}!")

class SubClass(BaseClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"I am {self.age} years old.")

sub_instance = SubClass("Mann", 20)

sub_instance.greet()