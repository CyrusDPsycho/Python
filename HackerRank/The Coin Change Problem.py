
t, n = map(int, raw_input().split())
nums = map(int, raw_input().split())
dp = [[0]*(t+1) for _ in xrange(n+1)]
for i in xrange(n+1):
    dp[i][0] = 1
for i in xrange(1, n+1):
    for j in xrange(1, t+1):
        dp[i][j] = dp[i-1][j]
        if j >= nums[i-1]:
            dp[i][j] += dp[i][j-nums[i-1]]
print dp[-1][-1]
