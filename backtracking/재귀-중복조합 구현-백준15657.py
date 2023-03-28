import sys
input = sys.stdin.readline


def solution(M,curr,ipt):
    if M==1:
        for i in ipt:
            curr.append(i)
            rst.append(sorted(curr))
            curr.pop(curr.index(i))
    else:
        for idx,i in enumerate(ipt):
            curr.append(i)
            solution(M-1,curr,ipt[idx:])
            curr.pop(curr.index(i))

n,m = map(int,input().split())
temp = sorted(list(map(int,input().split())))

rst = []
solution(m,[],temp)
for i in rst:
    for j in i:
        print(j,end=" ")
    print()

