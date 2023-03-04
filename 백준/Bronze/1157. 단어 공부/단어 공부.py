string = input().upper()
number = 0
result = []

for i in list(set(string)):
    if string.count(i) > number:
        number = string.count(i)
        result = []
        result.append(i)
    elif string.count(i) == number:
        result.append(i)
    else:
        pass
if len(result) == 1:
    print(result[0])
elif len(result) >= 2:
    print('?')
    