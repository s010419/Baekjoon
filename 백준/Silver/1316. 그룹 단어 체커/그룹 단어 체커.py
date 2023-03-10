N = int(input())
result = 0

for _ in range(N):
    string = input()
    list_index = []
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            list_index.append(i-1)
        else:
            pass
    list_s = list(string)
    reversed_index = list(reversed(list_index))
    for j in range(len(list_index)):
        list_s.pop(reversed_index[j]) 
    if len(list_s) == len(set(list_s)):
        result += 1
    else:
        pass 

print(result)