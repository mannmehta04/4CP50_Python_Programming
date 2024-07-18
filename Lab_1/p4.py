import math

a, b, c = map(float, input("Enter a, b, c: ").split())
d = b**2 - 4*a*c
msg = "The roots are {}"
print(msg.format("real and distinct.")) if d > 0 else print(msg.format("real and equal.")) if d == 0 else print(msg.format("complex and distinct."))
if d >= 0:
    print(f"Root 1 = {(-b + math.sqrt(d)) / (2*a)}")
    if d > 0:
        print(f"Root 2 = {(-b - math.sqrt(d)) / (2*a)}")
else:
    real_part = -b / (2*a)
    img_part = math.sqrt(-d) / (2*a)
    print(f"Root 1 = {real_part} + {img_part}i")
    print(f"Root 2 = {real_part} - {img_part}i")