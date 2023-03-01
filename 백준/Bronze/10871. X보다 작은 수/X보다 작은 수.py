N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []

for i in A:
    if X > i:
        result.append(i)
    else:
        pass
print(' '.join(map(str, result)))