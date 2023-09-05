def cal(grp):
    curr = 0
    ans = 0
    container = []
    while curr<len(grp):
        for i in range(len(container)):
            if container[i]<grp[curr]:
                ans+=container[i]*2
        ans+=grp[curr]
        container.append(grp[curr])
        curr+=1
    return ans - sum(grp)


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

graph = deque()
graph2 = [[] for _ in range(M)]
for _ in range(N):
    P,W = map(int,input().split())
    graph.append((P,W))
    graph2[P-1].append(W)

answer = 0
curr = M
cnt = len(graph2[curr-1])
while curr>0:
    con = []
    while cnt>0:
        p,w = graph.popleft()
        if p == curr:
            cnt-=1
            con.append(w)
            answer += w
        else:
            answer += w
            graph.append((p, w))
    answer+=cal(con)
    curr-=1
    cnt=len(graph2[curr-1])
print(answer)
