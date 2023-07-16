def solution(s):
    open = 0
    close = 0
    
    for i in s:
        if i == '(':
            open += 1
        else :
            close += 1
        if open < close:
            return False
        
    if open != close:
        return False
    return True




# def solution(s):
#     while True:
#         if '()' in s:
#             s = s.replace('()', '')
#         else:
#             break
            
#     if s == '':
#         return True
#     else :
#         return False