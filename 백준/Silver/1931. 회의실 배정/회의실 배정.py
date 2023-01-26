import sys
num = int(sys.stdin.readline())

list_ = []
for _ in range(num):
    list_.append(tuple(map(int, sys.stdin.readline().split())))

list_.sort(key = lambda x : [x[1], x[0]])

ed = 0
cnt = 0
for s, e in list_:
    if s >= ed:
        cnt += 1
        ed = e
print(cnt)