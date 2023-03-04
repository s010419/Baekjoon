num = input().split()
if int((num[0][::-1])) > int(num[1][::-1]):
    print(int(num[0][::-1]))
elif int(num[0][::-1]) < int(num[1][::-1]):
    print(int(num[1][::-1]))