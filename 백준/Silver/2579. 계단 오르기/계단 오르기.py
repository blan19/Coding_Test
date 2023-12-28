from sys import stdin as s

# s = open("input.txt", 'rt')

N = int(s.readline().rstrip())
stairs = [int(s.readline().rstrip()) for _ in range(N)]

dp = [0] * N

if N <= 2:
  print(sum(stairs))
else:
  dp[0] = stairs[0]
  dp[1] = stairs[0] + stairs[1]
  
  for i in range(2, N):
    dp[i] = max(dp[i - 3] + stairs[i] + stairs[i - 1], dp[i - 2] + stairs[i])
    
  print(dp[-1])