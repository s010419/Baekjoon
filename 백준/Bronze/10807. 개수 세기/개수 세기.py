N = int(input())
list = map(int, input().split())
v = int(input())
number = 0

for i in list:
    if v == i:
        number += 1
    else:
        pass
print(number)