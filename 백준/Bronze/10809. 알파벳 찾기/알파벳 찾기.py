string = input()
result = []

for i in range(97, 123):
    try:
        string.index(chr(i))
        result.append(string.index(chr(i)))
    except:
        result.append(-1)
print(' '.join(map(str, result)))