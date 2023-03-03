n, m = map(int, input().split())

baskets = [0] * n

for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a-1, b):
        baskets[j] = c

for d in baskets:
    print(d, end=' ')