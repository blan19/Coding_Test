import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

data.sort(key=lambda x : (x[1], x[0]))

count = 1
prev_end_time = data[0][1]

for i in range(1, N):
  if prev_end_time <= data[i][0]:
    prev_end_time = data[i][1]
    count += 1

print(count)