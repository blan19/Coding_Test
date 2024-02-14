def solution(friends, gifts):
  take = {}
  give = {}
  answer = {}
  max_num = 0
  
  for friend in friends:
    take[friend] = []
    give[friend] = []
    answer[friend] = 0
  
  for gift in gifts:
    a, b = gift.split(" ")
    
    give[a].append(b)
    take[b].append(a)
  
  for i in range(0, len(friends)):
    for j in range(i + 1, len(friends)):
      give_count = give[friends[i]].count(friends[j])
      take_count = take[friends[i]].count(friends[j])
      a_gift_point = len(give[friends[i]]) - len(take[friends[i]])
      b_gift_point = len(give[friends[j]]) - len(take[friends[j]])
      
      # 선물을 주고 받은 기록이 있을 때
      if give_count > 0 or take_count > 0:
        # 주고 받은 선물이 존재하고 선물 갯수가 같다면
        if give_count == take_count:
          if a_gift_point > b_gift_point:
            answer[friends[i]] += 1
          elif b_gift_point > a_gift_point:
            answer[friends[j]] += 1
          else:
            answer[friends[i]] += 0
        else:
          # 주고 받은 선물 갯수가 다를 때
          if give_count > take_count:
            answer[friends[i]] += 1
          else:
            answer[friends[j]] += 1
      else: # 선물을 주고 받은 기록이 없을 때
        if a_gift_point > b_gift_point:
            answer[friends[i]] += 1
        elif b_gift_point > a_gift_point:
            answer[friends[j]] += 1
            
  for count in answer.values():
    if max_num < count:
      max_num = count
      
  return max_num