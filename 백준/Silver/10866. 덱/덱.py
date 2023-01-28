import sys
num = int(sys.stdin.readline())

deque = []
for _ in range(num):
    txt = sys.stdin.readline().strip()
    if 'push_front' in txt:
        deque.insert(0, int(txt.split()[1]))
        
    elif 'push_back' in txt:
        deque.append(int(txt.split()[1]))
    
    elif txt == 'pop_front':
        try:
            print(deque.pop(0))
        except :
            print(-1)
    elif txt == 'pop_back':
        try:
            print(deque.pop())
        except :
            print(-1)
    elif txt == 'size':
        print(len(deque))
    elif txt == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif txt == 'front':
        try:
            print(deque[0])
        except:
            print(-1)
    elif txt == 'back':
        try:
            print(deque[-1])
        except:
            print(-1)
        
        



            

            
            









