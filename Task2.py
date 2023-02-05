s = int(input("S = "))
p = int(input("P = "))

for x in range(1000):
    for y in range(1000):
        if x + y == s and x * y == p:
            print(f"x = {x}; y = {y}")
