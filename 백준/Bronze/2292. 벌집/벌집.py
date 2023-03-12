N = int(input())
number = 1
result = 1

while True:
    if N <= number:
        break
    else:
        number += 6*result
        result += 1

print(result)