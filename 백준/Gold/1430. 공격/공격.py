import collections
import math

N, R, D, TX, TY = map(int,input().split())
towers = {tuple(map(int, input().split(" "))) for _ in range(N)}

def solution():
  queue = collections.deque()
  
  queue.append((TX, TY, 0))
  
  answer = bfs(queue)
  
  if int(answer) != answer:
    print(answer)
  else:
    print(f'{answer}.0')

def bfs(queue):
  global towers
  answer = 0
  
  while queue:
    x, y, level = queue.popleft()
    
    if(level):
      answer += D / (2**(level - 1))
    
    valid_range_tower = []
    
    for t in towers:
      if isRange(x, y, t[0], t[1]):
        valid_range_tower.append(t)
        
    for t in valid_range_tower:
      queue.append((t[0], t[1], level + 1))
    
    towers -= set(valid_range_tower)
  
  return answer


def isRange(x, y, nx, ny):
  if math.sqrt((x - nx)**2 + (y - ny)**2) <= R:
    return True
  return False

solution()