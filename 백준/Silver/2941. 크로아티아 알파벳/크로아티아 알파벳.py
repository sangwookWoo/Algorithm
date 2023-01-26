import sys
string = sys.stdin.readline()
list_ = ['dz=', 'lj','nj','c=', 'c-', 'd-','s=','z=']
cnt = 0

for i in list_:
    if i in string:
        cnt += string.count(i)
        string = string.replace(i, '|')
string = string.replace('|', '')
print(cnt + len(string.strip()))