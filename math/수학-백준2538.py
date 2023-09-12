N  = int(input())
lst = sorted(list(map(int,input().split())))
ans = [0 for _ in range(N)]
for i in range(1,N):
    ans[0]+= abs(lst[0]-lst[i])
for i in range(1,N):
    d = lst[i] - lst[i-1]
    #i-1개 x #N-i-1개 -x -> 생각해보니 이 논리면 정렬 후 가운데 값이 가장 작음
    ans[i] = ans[i-1] + ((i-1)*d-(N-i-1)*d)

print(lst[ans.index(min(ans))])