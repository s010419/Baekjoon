A, B = map(int, input().split())

if A >= 0 and B - 45 >= 0:
    print("%d"%A +" "+ "%d"%(B-45))
elif B - 45 < 0:
    A = A - 1
    if A >= 0:
        print("%d"%A +" "+ "%d"%(60-(45-B)))
    else:
        print("%d"%(24+A) +" "+ "%d"%(60-(45-B)))
