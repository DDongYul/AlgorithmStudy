import sys
input = sys.stdin.readline

N,L = map(int,input().split())
cnt = 0
mx = 0
for _ in range(N):
    z = input().strip()
    curr = 0
    flag = True
    for i in z:
        if i == '1' and flag:
            curr+=1
            flag = False
        elif i == '1' and not flag:
            continue
        else:
            flag = True

    if mx<curr:
        cnt=1
        mx = curr
    elif mx == curr:
        cnt+=1

print(mx,cnt)
