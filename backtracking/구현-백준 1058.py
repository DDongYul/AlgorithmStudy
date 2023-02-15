import sys

friend_list = []
N=int(sys.stdin.readline())
for i in range(0,N):
    friend_list.append((sys.stdin.readline().split()))

result = []
for i in range(0,N):
    for j in range(0,N):
        if friend_list[i][0][j] == 'Y':
            result.append((i,j))                #직접 친구인 경우

for i in range(0,N):
    for j in range(0,N):
        for k in range(j+1,N):
            if friend_list[i][0][j] == 'Y' and friend_list[i][0][k] == 'Y':
                if (j,k) not in result:
                    result.append((j,k))
                    result.append((k, j))       #2-친구인 경우

dic = {}
for i in result:
    if i[0] in dic:
        dic[i[0]] +=1
    else:
        dic[i[0]] = 1

if dic:
    print(max(dic.values()))
else:
    print(0)
