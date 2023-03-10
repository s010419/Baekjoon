final_sum = 0
credit_sum = 0
grade_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0 }

try:
    for _ in range(20):
        string, credit, grade = input().split()
        if grade == 'P':
            pass
        else:
            final_sum += float(credit)*float(grade_dic[grade])
            credit_sum += float(credit)
        
except:
    pass

print('%.6f' %(final_sum/credit_sum))