number = list(map(int, input().split()))
piece = [1,1,2,2,2,8]
result = []

for i in range(6):
    result.append(piece[i]-number[i])
print(' '.join(map(str, result)))