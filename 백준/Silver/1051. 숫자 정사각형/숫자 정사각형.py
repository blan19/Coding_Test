N, M = map(int,input().split())
data = [list(input()) for _ in range(N)]

def solution(n, m, data):
  check = min(n, m)
  answer = 0
  for i in range(n):
    for j in range(m):
      for k in range(check):
        if ((i + k) < n) and ((j + k) < m) and (data[i][j] == data[i][j + k] == data[i + k][j] == data[i + k][j + k]):
          answer = max(answer, (k + 1)**2)
            
  return answer
  
print(solution(N, M, data))