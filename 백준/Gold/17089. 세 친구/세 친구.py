import sys
import math

N, M = map(int, sys.stdin.readline().split(" "))
data = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

def solution():
  relations = [[False for _ in range(N + 1)] for _ in range(N + 1)]
  count = [0 for _ in range(N + 1)]
  answer = math.inf
  
  for d in data:
    a, b = d
    relations[a][b] = True
    relations[b][a] = True
    count[a] += 1
    count[b] += 1
  for i in range(N + 1):
    for j in range(i + 1, N + 1):
      if not relations[i][j]:
        continue
      for k in range(j + 1, N + 1):
        if not relations[i][k] or not relations[j][k]:
          continue
        answer = min(answer, count[i] + count[j] + count[k] - 6)

  if answer == math.inf:
    print(-1)
  else:
    print(answer)


solution()