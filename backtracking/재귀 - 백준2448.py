N = int(input())
star = [[' ' for _ in range(N*2)] for _ in range(N)]

def go(x, y, n):
    if n <= 3:
        star[x][y] = "*"
        star[x+1][y-1] = star[x+1][y+1] = "*"
        star[x + 2][y - 2] = star[x + 2][y - 1] = "*"
        star[x + 2][y + 2] = star[x + 2][y + 1] = "*"
        star[x+2][y] = "*";
        return
    m = n // 2
    go(x, y, m)
    go(x+m, y-m, m)
    go(x+m, y+m, m)

go(0, N-1, N)

for i in range(N):
    print("".join(star[i]))