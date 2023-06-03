import sys
N,K = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

index_list = []
for index,i in enumerate(data):
    if i == 1:
        index_list.append(index)

result = 9999999
if len(index_list) <K:
    result = -1
elif len(index_list) == K:
        result = index_list[K-1] - index_list[0]+1
else:
    for i in range(0,len(index_list)-(K-1)):
        temp = (index_list[i+K-1] - index_list[i]) +1
        if temp < result:
            result = temp

print(result)