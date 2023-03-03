N, M = map(int, input().split())

list = []

for k in range(1,N+1):
    list.append(k)

for _ in range(M):
    i, j = map(int, input().split())
    list[i-1], list[j-1] = list[j-1], list[i-1]
    
print(' '.join(map(str, list)))