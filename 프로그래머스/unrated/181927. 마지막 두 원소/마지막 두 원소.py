def solution(num_list):
    end_num = num_list[len(num_list) - 1]
    second_end_num = num_list[len(num_list) - 2]
    
    if end_num > second_end_num:
        num_list.append(end_num - second_end_num)
    else:
        num_list.append(end_num * 2)
        
    return num_list