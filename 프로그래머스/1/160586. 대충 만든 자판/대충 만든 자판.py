def solution(keymap, targets):
    dic = {};
    answer = []
    
    for str in keymap:
        for i in range(len(str)):
            if(dic.get(str[i]) != None):
                dic.update({ str[i]: min(dic.get(str[i]), i) })
            else:
                dic.update({ str[i]: i })
    # 최솟값을 매핑한 딕셔너리를 만든다
    print(dic)
    for target in targets:
        sum = 0
        print(len(target))
        for i in range(len(target)):
            value = dic.get(target[i])
            
            if value != None:
                sum += value + 1
            else:
                sum = -1
                break

        answer.append(sum)
        
    return answer


# 순회하면서 각 문자의 min 값을 찾아서 할당