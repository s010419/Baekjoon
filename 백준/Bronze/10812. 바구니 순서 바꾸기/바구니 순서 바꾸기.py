N, M = map(int, input().split())
result = []

for num in range(1,N+1):
    result.append(num)
for _ in range(M):
    i, j, k = map(int, input().split())
    repeat = result[k-1:j] + result[i-1:k-1]
    result[i-1:j] = repeat

print(' '.join(map(str, result)))