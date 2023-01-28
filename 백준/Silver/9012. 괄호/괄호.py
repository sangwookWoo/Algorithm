import sys
num = int(sys.stdin.readline())

for _ in range(num):
    stack = sys.stdin.readline().strip()
    while True:
        if '()' in stack:
            stack = stack.replace('()','')
        else :
            if len(stack) == 0:
                print('YES')
                break
            else :
                print('NO')
                break