

def solution(s):
    answer = []
    
    full_cnt = 0
    zero_cnt = 0
    while True:
        cnt = 0
        if s == '1':
            break

        # 0 카운트
        
        for i in s:
            if i == '0':
                cnt += 1
        
        # 0 대체
        s = s.replace('0', '')
        
        # 이진 변환
        s = bin(len(s))[2:]
        full_cnt += 1
        zero_cnt += cnt
            
            
        
    return [full_cnt, zero_cnt]
    
            
    
    
