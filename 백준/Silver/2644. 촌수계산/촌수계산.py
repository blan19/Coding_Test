import sys
from collections import deque

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split(" "))
M = int(sys.stdin.readline())

relatios = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
answer = 0

for _ in range(M):
  x, y = map(int, sys.stdin.readline().split(" "))
  relatios[x].append(y)
  relatios[y].append(x)
  
queue = deque()

queue.append((relatios[A], 1))

while queue:
  target, level = queue.popleft()
  
  for n in target:
    if visited[n]:
      continue
    if n == B:
      answer = level
      break
    
    visited[n] = True
    queue.append((relatios[n], level + 1))

if answer == 0:
  print(-1)
else:
  print(answer)