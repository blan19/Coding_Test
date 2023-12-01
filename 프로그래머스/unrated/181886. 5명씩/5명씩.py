def solution(names):
    count = 0
    answer = []
    
    for name in names:
        if count % 5 == 0:
            answer.append(name)

        count += 1
        
    return answer