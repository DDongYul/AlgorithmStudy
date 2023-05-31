import sys
N = int(input())
l = list(map(int,sys.stdin.readline().split()))
result = []
def sol(curr,li):
    if len(li) >2:
        for i in range(1,len(li)-1):
            w = li[i-1] * li[i+1]
            temp =li.copy()
            temp.pop(i)
            sol(curr+w,temp)
    else:
        result.append(curr)

sol(0,l)
print(max(result))