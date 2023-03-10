string = input()
c_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
result = 0

for i in c_list:
    result += string.count(i)
    string = string.replace(i, ' ')
string = string.replace(' ', '')
result += len(string)
print(result)