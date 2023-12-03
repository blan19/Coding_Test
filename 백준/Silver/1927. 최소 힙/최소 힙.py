import sys
from queue import PriorityQueue

K = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(K)]

def solution():
  pqueue = PriorityQueue()
  
  for num in data:
    if num == 0:
      size = pqueue.qsize()
      if size == 0:
        print(0)
      else:
        print(pqueue.get())
    else:
      pqueue.put(num)

solution()
