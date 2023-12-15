from sys import stdin as s

N = int(s.readline().rstrip())
dp =  [list(map(int, s.readline().split(" "))) for _ in range(N)]

for i in range(1, N):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
  
print(min(dp[N - 1]))