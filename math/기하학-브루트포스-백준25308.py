import itertools
import math


def sol(a,b,c):
    if(a*c*math.sqrt(2))<=(b*(a+c)):
        return True

lst = list(map(int,input().split()))
cnt = 0
per = itertools.permutations(lst,8)
for i in list(per):
    flag=True
    for j in range(8):
        if not sol(i[j-2],i[j-1],i[j]):
            flag = False
    if flag:
        cnt+=1
print(cnt)

