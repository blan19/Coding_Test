import sys
import math
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
data = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

def solution():
  relations = [set() for _ in range(N + 1)]
  min = math.inf
  answer = 0
  
  for d in data:
    a, b = d
    relations[a].add(b)
    relations[b].add(a)
  
  for i in range(N + 1):
    queue = deque()
    visited = [False for _ in range(N + 1)]
    friends = relations[i]
    count = 0
    
    if i == 0:
      continue
    
    queue.append((friends, 1))
    visited[i] = True
    
    while queue:
      friends, level = queue.popleft()
      
      for friend in friends:
        if visited[friend]:
          continue
        visited[friend] = True
        count += level
        queue.append((relations[friend], level + 1))
    
    if min > count:
      min = count
      answer = i
  
  print(answer)

solution()