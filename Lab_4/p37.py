def outside(a):
    def inside(b):
        print(f"from b:",b)
    print(f"from a:",a)
    inside(10)

outside(5)