import math
import sys
input = sys.stdin.readline

def gcd(x,y):
    if x<y: x,y=y,x
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)

n = int(input())
num = sorted([int(input()) for _ in range(n)])
num2= [(num[i]-num[i-1]) for i in range(1,n)]

curr_gcd = num2[0]
for i in range(1,n-1):
    curr_gcd = gcd(curr_gcd,num2[i])

m = []
for i in range(2,int(math.sqrt(curr_gcd))+1):
    if curr_gcd%i == 0:
        m.append(i)
        m.append(int(curr_gcd/i))
m.append(curr_gcd)
for i in sorted(list(set(m))):
    print(i,end=' ')