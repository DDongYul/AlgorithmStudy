dp = [0 for _ in range(101)]
dp[1] = 1
for i in range(2,101):
    dp[i] = dp[i-1]*2 + 1

cnt = 0
def hanoi(n, a, b, c):
    global cnt
    if n == 1:
        cnt+=1
        print(a, c, sep = " ")
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

n = int(input())
print(dp[n])
if n<=20:
    hanoi(n,1,2,3)

print(dp[n],cnt)