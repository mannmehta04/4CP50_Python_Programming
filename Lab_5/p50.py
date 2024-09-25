class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Default Area is 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(f"Area is {self.length ** 2}.")

square = Square(5)
square.area()