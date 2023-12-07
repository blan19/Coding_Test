import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
  p = sys.stdin.readline().rstrip()
  n = int(sys.stdin.readline().rstrip())
  data = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
  count = 0
  flag = False
  
  if n == 0:
    data = []
    
  for command in p:
    if command == "R":
      count += 1
    else:
      if len(data) == 0:
        print("error")
        flag = True
        break
      else:
        if count % 2 == 0:
          data.popleft()
        else:
          data.pop()
  
  if not flag:
    if not count % 2 == 0:
      data.reverse()
      print("["+",".join(data)+"]")
    else:
      print("["+",".join(data)+"]")