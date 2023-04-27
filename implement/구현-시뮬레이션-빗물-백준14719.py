#고이는 물은 왼쪽 오른쪽 끝까지 갔을 때 무조건 벽이 있어야한다!
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
block = list(map(int,input().split()))
for idx,c in enumerate(block):
    for i in range(c):
        graph[i][idx] = 1

answer = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            flag1 = False
            flag2 = False
            curr = j
            while curr>=0:
                if graph[i][curr] == 1:
                    flag1 = True
                    break
                curr-=1
            curr = j
            while curr<n:
                if graph[i][curr] == 1:
                    flag2 = True
                    break
                curr+=1
            if flag1 and flag2:
                answer +=1

print(answer)



