def solution(edges):
  input = {}
  output = {}
  size = 0
  answer = [0 for _ in range(4)]
  
  for o, i in edges:
    if output.get(o):
      output[o] += 1
    else:
      output[o] = 1
      
    if input.get(i):
      input[i] += 1
    else:
      input[i] = 1
    
    size = max([size, i, o])
  
  for i in range(1, size + 1):
    if not input.get(i) and output.get(i) >= 2:
      answer[0] = i
      
    if input.get(i) and output.get(i) and input.get(i) >= 2 and output.get(i) >= 2:
      answer[3] += 1
    
    if not output.get(i):
      answer[2] += 1
      
  answer[1] = output.get(answer[0]) - (answer[2] + answer[3])
  
  return answer