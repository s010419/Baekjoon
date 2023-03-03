N = int(input())
A = list(map(int, input().split()))
M = max(A)
B = []

for num in A:
    B.append(num/M*100)

print(sum(B)/N)