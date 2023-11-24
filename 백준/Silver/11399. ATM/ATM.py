N = input()
data = list(map(int, input().split()))

def solution(_, data):
  summary = 0
  answer = list()
  
  data.sort()
  
  for time in data:
    summary = time + summary
    answer.append(summary)

  
  print(sum(answer))
  
solution(N, data)