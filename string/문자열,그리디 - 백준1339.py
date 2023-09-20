import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    voc = input().strip()
    cnt = pow(10,len(voc)-1)
    for i in voc:
        if i in dic:
            dic[i] += cnt
        else:
            dic[i] = cnt
        cnt //= 10

lst = sorted(list(dic.values()),reverse=True)

ans = 0
cnt = 9
for i in lst:
    ans+= cnt*i
    cnt-=1
print(ans)

