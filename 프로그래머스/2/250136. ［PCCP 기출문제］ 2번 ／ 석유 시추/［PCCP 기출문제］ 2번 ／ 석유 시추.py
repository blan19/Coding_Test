from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(land):
  n = len(land)
  m = len(land[0])
  visited = [[False for _ in range(m)] for _ in range(n)]
  answer = []
  id = 1
  dic = {}
  
  for i in range(m):
    oil = 0
    s = set([])
    
    for j in range(n):
      if land[j][i] == 0:
        continue
      if visited[j][i] != 0:
        s.add(visited[j][i])
        continue
      
      oil = bfs(n, m, j, i, visited, land, id)
      dic[id] = oil
      s.add(visited[j][i])
      id += 1
    
    if len(s):
      total_oil_size = 0
      for i in s:
        total_oil_size += dic[i]
        
      answer.append(total_oil_size)
      
  return max(answer)

def bfs(n, m, x, y, visited, land, id):
  oil = 1
  queue = deque()
  queue.append((x, y))
  visited[x][y] = id
  
  while queue:
    cx, cy = queue.popleft()

    for pos in range(4):
      nx = dx[pos] + cx
      ny = dy[pos] + cy
      if nx < 0 or nx >= n or ny < 0 or ny >= m or land[nx][ny] == 0:
        continue
      if visited[nx][ny] != 0:
        continue
      visited[nx][ny] = id
      oil += 1
      queue.append((nx, ny))

  return oil