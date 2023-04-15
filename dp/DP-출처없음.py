def solution(n, k):
    # k보다 작은 값은 곱셈을 위해 1 유효값은 덧셈 계산을 위해 0 설정
    dp = [1 for _ in range(n + 1)]
    for i in range(k + 1, n + 1):
        dp[i] = 0

    # 초기값
    if k % 2 == 0:
        dp[k + 1] = 1
        dp[k + 2] = 2
    else:
        dp[k + 1] = 2
        dp[k + 2] = 3

    # 탐색 4가지 case(n,k가 짝/홀)
    for i in range(k + 3, n + 1):
        if i % 2 == 0:
            if int(i / 2) == k:  # 1,2번 케이스가 경우 같을 때
                dp[i] += dp[i - k]
            else:
                dp[i] += dp[i - k]
                dp[i] += dp[int(i / 2)] * dp[int(i / 2)]
        else:
            if k % 2 == 0:
                dp[i] += dp[i - k]
            else:
                if i == k * 3:  # 1,3번 케이스가 경우 같을 때 -> k,2k로 나누어질때
            dp[i] += dp[i - k]
            dp[i] += dp[i - k]
            q = int((n - k) / 2)
            p = q + k
            dp[i] += dp[p] * dp[q]
    dp[i] = dp[i] % 10007
    return dp[n]

n1, k1 = map(int, input().split())
print(solution(n1, k1))

# n=7 k=3
# 7 -> [5,2] -> [2,2,3]
# 7 -> [5,2] -> [4,1,2] -> [2,2,1,2]
# 7 -> [5,2] -> [4,1,2] -> [1,3,1,2]
# 7 -> [4,3] -> [2,2,3]
# 7 -> [4,3] -> [1,3,3]