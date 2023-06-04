import sys
input = sys.stdin.readline

def per(arr,n):
    rst = []
    if n>len(arr):
        return
    if n == 1:
        for i in arr:
            rst.append([i])
    else:
        curr = per(arr,n-1)
        for j in range(len(curr)):
            k = curr.pop()
            for i in range(1,N+1):
                if i >= k[-1]:
                    rst.append(k+[i])
    return sorted(rst)

N,M = map(int,input().split())
num = [i for i in range(1,N+1)]
result = per(num,M)
for i in result:
    for j in i:
        print(j, end= " ")
    print()