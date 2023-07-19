import sys
import re
from collections import deque




while True:
    
    data = input()
    cnt = 0
    if data == '.':
        break

    stack = deque()
    
    for i in data:
        
        if i in ['(', '[']:
            stack.append(i)
        
        if i in [')', ']']:
            cnt += 1
        
        if len(stack) != 0:
            if i == ')' and stack[-1] == '(':
                stack.pop()
                cnt -= 1
            
            elif i == ']' and stack[-1] == '[':
                stack.pop()
                cnt -= 1

    
    if cnt == 0 and len(stack) == 0:
        print('yes')
    else:
        print('no')