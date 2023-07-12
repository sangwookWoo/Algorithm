from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    
    # today 날짜형식 변환
    today = datetime.strptime(today, '%Y.%m.%d')
    
    # terms 딕셔너리로 변환
    terms_p = {}
    for term in terms:
        yg, month = term.split(' ')
        terms_p[yg] = int(month)
    
    # privacies 비교
    for idx, p in enumerate(privacies):
        p_date, p_yg = p.split(' ')
        p_date = datetime.strptime(p_date, '%Y.%m.%d')
        expire_date = p_date + relativedelta(months = terms_p[p_yg])
        if expire_date <= today:
            answer.append(idx + 1)
        
    return answer