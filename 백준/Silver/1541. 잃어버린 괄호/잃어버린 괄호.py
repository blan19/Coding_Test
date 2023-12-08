import sys

expression = sys.stdin.readline().rstrip().split("-")
numbers = []
answer = 0
flag = False

for ex in expression:
  plus_expression = list(map(int,ex.split("+")))
  sum = 0
  
  for num in plus_expression:
    sum += num
  
  if not flag:
    answer += sum
  else:
    answer -= sum
  
  flag = True

print(answer)