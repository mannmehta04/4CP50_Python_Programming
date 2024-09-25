class height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        extra_feet = total_inches // 12
        new_inches = total_inches % 12
        new_feet = self.feet + other.feet + extra_feet
        return height(new_feet, new_inches)

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

print(height(4, 3) + height(5, 9))