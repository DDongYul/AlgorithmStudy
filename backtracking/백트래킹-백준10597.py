def search(idx,lst,v):
    if all(v):
         rst.append(lst[:])
         return
    #한글자
    if idx<len(sq):
        curr = int(sq[idx])
        if curr<=n:
            if not v[curr] and curr not in lst:
                v1=v.copy()
                v1[curr]=1
                lst1 = lst.copy()
                lst1.append(curr)
                search(idx+1,lst1,v1)
    #두글자
    if idx < len(sq)-1:
        curr_2 = int(sq[idx:idx+2])
        if curr_2 <= n:
            if not v[curr_2] and curr_2 not in lst:
                v2=v.copy()
                v2[curr_2] = 1
                lst2= lst.copy()
                lst2.append(curr_2)
                search(idx + 2, lst2, v2)

sq = input()
num = [0 for _ in range(51)]
cnt = 0
for i in range(1,51):
    if 0<i<10:
        cnt+=1
        num[i] = cnt
    elif 10<=i<=50:
        cnt+=2
        num[i]=cnt
for index,i in enumerate(num):
    if len(sq) == i:
        n = index

visited = [0 for i in range(n+1)]
visited[0] = 1
rst = []
search(0,[],visited)

result = list(map(str,rst[0]))
print(" ".join(result))




