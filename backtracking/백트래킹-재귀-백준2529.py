def check(a,b,op):
    if op == '<':
        return a<b
    elif op == '>':
        return a>b

n = int(input())
sign = list(input().split())
visited = [False for _ in range(10)]
max_ans = ""
min_ans = ""

def search(depth,s):
    global max_ans, min_ans
    if depth == n+1:
        if not len(min_ans):
            min_ans = s
            max_ans = s
        else:
            max_ans = s
        return
    for i in range(10):
        if visited[i]:
            continue
        if depth == 0 or check(int(s[-1]),i,sign[depth-1]):
            visited[i] = True
            search(depth + 1, s+str(i))
            visited[i] = False

search(0,"")

print(max_ans)
print(min_ans)



