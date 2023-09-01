import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

size = min(n,m)-1
answer = []

while size>0:
    for i in range(n):
        for j in range(m):
            if i+size<n and j+size<m:
                if graph[i][j] == graph[i+size][j] == graph[i][j+size] == graph[i+size][j+size]:
                    answer.append(size+1)
    size-=1
if answer:
    print(int(pow(max(answer),2)))
else:
    print(1)