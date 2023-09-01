import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    lst = sorted(list(map(int,input().split())))
    p1 = 0
    p2 = n-1
    rst = [0 for _ in range(n)]
    for i in range(n):
        if i%2:
            rst[p1] = lst[i]
            p1+=1
        else:
            rst[p2] = lst[i]
            p2-=1
    answer = abs(rst[-1] - rst[0])
    for i in range(n-1):
        answer = max(answer,abs(rst[i+1]-rst[i]))
    print(answer)
