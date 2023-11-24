K = int(input())

def solution(k):
  count = 0
  while k >= 0:
    if k % 5 == 0:
      count += k//5
      break
    elif k % 5 != 0 and k >= 3:
      k -= 3
      count += 1
    else:
      count = -1
      break
      
  print(count)

solution(K)