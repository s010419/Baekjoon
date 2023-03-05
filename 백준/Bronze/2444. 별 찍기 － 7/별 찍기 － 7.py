N = int(input())

for i in range(1,2*N):
    if i < N:
        string = '*'*(2*i-1)
        print(string.rjust(N+(i-1),' '))
    elif i == N:
        string = '*'*(2*i-1)
        print(string)   
    elif i > N:
        string = '*'*(4*N-1-2*i)
        print(string.rjust(3*N-1-i,' '))