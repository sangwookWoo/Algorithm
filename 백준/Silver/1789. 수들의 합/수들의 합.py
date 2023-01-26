import sys
num = int(sys.stdin.readline())

sum = 0
add_num = 1
cnt = 0
while True:
    sum += add_num
    add_num += 1
    cnt += 1
    if sum > num:
        cnt -= 1
        break
    

print(cnt)
    
    






