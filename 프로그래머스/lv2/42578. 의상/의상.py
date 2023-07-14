from itertools import product

def solution(clothes):
    vd = dict()
    cnt = 0
    vl = []
    
    # 초기화
    for clothe in clothes:
        vd[clothe[1]] = 0
        
    # 딕셔너리 생성
    for clothe in clothes:
        vd[clothe[1]] += 1
    
    # 각 리스트별 가지수 곱하기, 안입는 경우 추가(+ 1)
    first = 1
    for i in vd.values():
        first *= (i + 1)
    
    return first - 1
    