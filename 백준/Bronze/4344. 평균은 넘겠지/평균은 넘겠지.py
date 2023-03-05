C = int(input())

for _ in range(C):
    class_list = list(map(int, input().split()))
    average = sum(class_list[1:])/class_list[0]
    student = []
    for i in class_list[1:]:
        if i > average:
            student.append(i)
    result = len(student)/class_list[0]*100
    print(f'{result:.3f}%')