from collections import Counter

def solution(k, tangerine):
    answer = 1
    sum = 0
    counter = Counter(tangerine)
    arr = sorted(counter.values(), reverse=True)
    
    for count in arr:
        sum += count        
        if sum >= k:
            return answer
        answer += 1