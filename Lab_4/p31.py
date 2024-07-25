def call_by_value(x):
    x = 10
    print("Inside the function: x =", x)

def call_by_reference(x):
    x[0] = 10
    print("Inside the function: x =", x)

x = [1, 2, 3]
print("Before the function call: x =", x)
call_by_value(x)
print("After the function call: x =", x)
print()

x = [1, 2, 3]
print("Before the function call: x =", x)
call_by_reference(x)
print("After the function call: x =", x)