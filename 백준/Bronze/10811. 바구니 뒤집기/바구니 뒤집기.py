N, M = map(int, input().split())

basket = []

for k in range(1,N+1):
    basket.append(k)
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(' '.join(map(str, basket)))