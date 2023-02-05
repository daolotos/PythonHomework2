
n = int(input("N = "))
coins = []
a = 0  # количество решек
for i in range(n):
    coins.append(int(input(f"coin {i + 1} = ")))
    if coins[i] == 1:
        a += 1

b = n - a # количество орлов
minActions = min(a, b)

print(f"Min actions = {minActions}")
