import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

#Djk = min(Djk,Dji+Dik)
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

for _ in range(m):
    s,d,t = map(int,sys.stdin.readline().split())
    if graph[s-1][d-1]<=t:
        print("Enjoy other party")
    else:
        print("Stay here")


