def solution(bandage, health, attacks):
  time, healing, plus_healing = bandage
  last_attack_time = 0
  answer = health
    
  for attack_time, attack_health in attacks:
    add_health_point = ((attack_time - 1 - last_attack_time) * healing) + (((attack_time - 1 - last_attack_time) // time) * plus_healing)
    last_attack_time = attack_time

    if answer + add_health_point >= health:
      answer = health
    else:
      answer += add_health_point
    if answer - attack_health <= 0:
      return -1
    else:
      answer -= attack_health
  return answer