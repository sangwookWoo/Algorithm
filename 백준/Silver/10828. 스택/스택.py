import sys
num = int(sys.stdin.readline())

stack = []
for _ in range(num):
    jg_text = sys.stdin.readline().strip()
    if 'push' in jg_text:
        stack.append(int(jg_text.split()[-1]))  
    elif jg_text == 'pop':
        try:
            print(stack.pop(-1))
        except :
            print(-1)
    elif jg_text == 'size':
        print(len(stack))
    elif jg_text == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif jg_text == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
            
            

            
            









