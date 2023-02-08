def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def search(depth):
    global count
    if depth==n:
        count += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        row[depth] = i
        if check(depth):
            visited[i] = True
            search(depth+1)
            visited[i] = False

n = int(input())
row = [0] * n
visited = [False] * n
count = 0
search(0)
print(count)