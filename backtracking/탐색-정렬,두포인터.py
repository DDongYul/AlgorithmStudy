import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
start = 0
end = n-1

c = abs(lst[start] + lst[end])
answer = [lst[0],lst[-1]]

while start<end:
    s = lst[start] + lst[end]
    if  c>abs(s):
        answer[0] = lst[start]
        answer[1] = lst[end]
        c = abs(lst[start] + lst[end])
    if s>0:
        end-=1
    else:
        start+=1
print(answer[0],answer[1])
