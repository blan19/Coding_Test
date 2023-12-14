import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split(" "))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

graph = [[list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

queue = deque()

answer = 0
flag = False

def bfs():
  while queue:
    x, y, z = queue.popleft()
    
    for n in range(6):
      nx = x + dx[n]
      ny = y + dy[n]
      nz = z + dz[n]
      
      if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
        continue
      
      if graph[nx][ny][nz] == 0:
        graph[nx][ny][nz] = graph[x][y][z] + 1
        queue.append((nx, ny, nz))
        
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        queue.append((i, j, k))

bfs()

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 0:
        flag = True
    answer = max(answer, max(graph[i][j]))

if flag:
  print(-1)
else:
  print(answer - 1)