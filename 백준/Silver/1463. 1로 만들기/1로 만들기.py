import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * 1000001
dp[2] = 1
dp[3] = 1

def solution(N):
  if N <= 3:
    return dp[N]

  for i in range(4, N + 1):
    dp[i] = dp[i - 1] + 1
  
    if i % 2 == 0:
      dp[i] = min(dp[i], (dp[i//2] + 1))
    
    if i % 3 == 0:
      dp[i] = min(dp[i], (dp[i//3] + 1))

  return dp[N]
    
print(solution(N))