import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
visited = [0 for _ in range(N)]
answer = []

def sol(depth,curr):
    if depth == M:
        answer.append(curr)
        return
    prev = -1
    for i in range(N):
        if not visited[i] and ls[i] != prev:
            visited[i] = 1
            sol(depth+1,curr+[ls[i]])
            visited[i] = 0
            prev = ls[i]

sol(0,[])
for i in answer:
    a = list(map(str,i))
    print(" ".join(a))









