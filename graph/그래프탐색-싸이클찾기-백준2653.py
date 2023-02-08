import sys
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited = [0 for _ in range(n)]
rst = []

def search(start):
    visited[start] = 1
    lst = graph[start]
    temp = [start+1]
    for index,i in enumerate(graph):
        if not visited[index] and lst == i:
            temp.append(index+1)
            visited[index] = 1
    if len(temp) >1 :
        rst.append(temp)

for i in range(n):
    if not visited[i]:
        search(i)

cnt = 0
for i in rst:
    i.sort()
    for j in i:
        cnt+=1

if cnt==n:
    print(len(rst))
    for i in rst:
        for j in i:
            print(j,end=' ')
        print()
else:
    print(0)

