A, B, V = map(int, input().split())
result = 1

if A >= V:
    pass
else:
    if (V-A)//(A-B) == (V-A)/(A-B):
        result += (V-A)//(A-B)
    else:
        result += (V-A)//(A-B) + 1
    
print(result)