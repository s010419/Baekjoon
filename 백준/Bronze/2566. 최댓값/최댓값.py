result = []
maximum = []

for _ in range(9):
    list_num = list(map(int, input().split()))
    result.append(list_num)
    maximum.append(max(list_num))

print(max(maximum))

for i in range(9):
    string = ' '.join(map(str, result[i]))
    if string.find(str(max(maximum))) == -1:
        pass
    else:
        print('%d %d'%(i+1, result[i].index(max(maximum))+1))