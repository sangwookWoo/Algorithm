def solution(lottos, win_nums):


    cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        for win in win_nums:
            if lotto != 0:
                if lotto == win:
                    cnt += 1
            
                
    max_rank = 7 - cnt - zero_cnt
    min_rank = 7 - cnt
    
    if max_rank > 6:
        max_rank = 6
    if min_rank > 6:
        min_rank = 6
                
    
    return [max_rank, min_rank]