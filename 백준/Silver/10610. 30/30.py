import sys
num = list(sys.stdin.readline())
num.sort(reverse = True)
num = int(''.join(num))
if num % 30 == 0:
    print(num)
else:
    print(-1)