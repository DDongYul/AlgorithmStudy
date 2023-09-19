# 위상 정렬
# 위상 정렬이 가능하려면 그래프에 싸이클이 없어야 한다.
import sys
input = sys.stdin.readline

N, M = map(int,(input().split()))
graph = [[] for _ in range(N)]
dist = [0 for _ in range(N)] #차수(우선 순위)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)  # a-1 뒤에 b-1이 와야 한다.(간선과 같은 존재)
    dist[b-1]+=1    #b-1 앞에 누군가 있어야해서 차수(우선순위) 1개 뒤쳐짐

ans = []
queue = []
for i in range(N):  #우선 순위가 가장 앞인 것(우선순위 값0)을 큐에 초기 값으로 넣어준다.
    if dist[i] == 0:
        queue.append(i)

while queue:
    s = queue.pop()
    ans.append(str(s+1))
    for i in graph[s]:  #현재 사람이 줄을 섰을 때 연관된 사람의 차수를 줄여줌
        dist[i] -=1
        if dist[i] == 0:
            queue.append(i)

print(" ".join(ans))

