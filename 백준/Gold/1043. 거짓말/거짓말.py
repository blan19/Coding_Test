import collections

N, M = map(int,input().split())
know = list(map(int, input().split(" ")))
party = [list(map(int, input().split(" "))) for _ in range(M)]

def solution():
  graph = [[] for _ in range(N + 1)]
  visited = [False for _ in range(N + 1)]
  queue = collections.deque()
  
  for p in party:
    valid_party = p[1:]
    
    for v in valid_party:
      graph[v].extend(valid_party)
      
      
  for i in range(N + 1):
    graph[i] = list(set(graph[i]) - { i })
  
  for v in know[1:]:
    visited[v] = True
    queue.append(v)
    
  bfs(graph, visited, queue)
  
  result_know_people = set()
  answer = 0
  
  for i in range(N + 1):
    if(visited[i]):
      result_know_people.add(i)
  
  for p in party:
    valid_party = p[1:]
    
    if set(valid_party) == set(valid_party) - result_know_people:
      answer += 1
  
  return answer

def bfs(graph, visited, queue):
  while queue:
    nv = queue.popleft()
    for v in graph[nv]:
      if not visited[v]:
        visited[v] = True
        queue.append(v)
  
print(solution())