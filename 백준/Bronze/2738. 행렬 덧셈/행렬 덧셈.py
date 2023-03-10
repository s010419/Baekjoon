N, M = map(int, input().split())
A_number = []
B_number = []
result = []

for _ in range(N):
    A_num = list(map(int, input().split()))
    A_number.append(A_num)

for _ in range(N):
    B_num = list(map(int, input().split()))
    B_number.append(B_num)

for i in range(len(A_number)):
    final_list = []
    for j in range(M):
        final_list.append(A_number[i][j] + B_number[i][j])
    result.append(final_list)

for k in range(len(result)):
    print(' '.join(map(str, result[k])))