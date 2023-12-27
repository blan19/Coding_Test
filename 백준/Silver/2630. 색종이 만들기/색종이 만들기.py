from sys import stdin as s

# s = open("input.txt", 'rt')

N = int(s.readline().rstrip())
paper = [list(map(int, s.readline().rstrip().split(" "))) for _ in range(N)]
answer = []


def recur(x, y, n):
  for i in range(x, x + n):
    for j in range(y, y + n):
      if paper[x][y] != paper[i][j]:
        recur(x, y, n // 2)
        recur(x, y + n // 2, n // 2)
        recur(x + n //2, y, n // 2)
        recur(x + n // 2, y + n //2, n // 2)
        return
  if paper[x][y] == 0:
    answer.append(0)
  else:
    answer.append(1)

recur(0, 0, N)
print(answer.count(0))
print(answer.count(1))