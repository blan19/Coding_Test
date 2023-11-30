import sys

K, N = map(int,input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

def solution():
  start = 1
  end = max(lan)
  result = []
  
  while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for l in lan:
      total += l // mid
      
    if total < N:
      end = mid -1
    else:
      start = mid + 1
      result.append(mid)
  
  answer = max(result)
  
  return answer

print(solution())