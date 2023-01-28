import sys
num = int(sys.stdin.readline())

queue = []
for _ in range(num):
    jg_text = sys.stdin.readline().strip()
    if 'push' in jg_text:
        queue.append(int(jg_text.split()[-1]))  
    elif jg_text == 'pop':
        try:
            print(queue.pop(0))
        except :
            print(-1)
    elif jg_text == 'size':
        print(len(queue))
    elif jg_text == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif jg_text == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif jg_text == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)
            
            

            
            









