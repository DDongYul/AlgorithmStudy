import math

n,k = map(int,input().split())
cnt = int(math.pow(2,n-k))
result = [[] for _ in range(cnt)]
N = int(math.pow(2,n))
K = int(math.pow(2,k))
arr = [str(i) for i in range(0,N)]

p1 = 0
p2 = N-1
while p1 < p2:
    result[p1%cnt].append(arr[p1])
    result[p1%cnt].append(arr[p2])
    p1+=1
    p2-=1

for i in result:
    print(" ".join(i))