import sys
input = sys.stdin.readline
dic = {}
n = int(input())
for _ in range(n):
    a,b = input().strip().split('.')
    if b in dic:
        dic[b] +=1
    else:
        dic[b] = 1
result = []
for i in dic:
    result.append((i,dic[i]))
result.sort()
for i,cnt in result:
    print(i ,cnt)