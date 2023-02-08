import sys
input = sys.stdin.readline

N,M = map(int,input().split())
true_list = set(list(map(int,input().split()))[1::])
party_list = []
# true_map = [0 for _ in range(N+1)]
# for i in true_list[1::]:
#     true_map[i] = 1
for _ in range(M):
    party_list.append(list(map(int,input().split()))[1::])

for _ in range(M):
    for i in party_list:
        for j in i:
            if j in true_list:
                true_list = true_list.union(i)
                break

count = M
for i in party_list:
    for j in i:
        if j in true_list:
            count-=1
            break
print(count)
