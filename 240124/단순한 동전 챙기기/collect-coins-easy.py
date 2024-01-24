import sys

n = int(input())

arr = [
    list(input())
    for _ in range(n)
]

s,e = (-1,-1),(-1,-1)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S':
            s = (i,j)
        elif arr[i][j] == 'E':
            e = (i,j)

tmp = list()
for num in range(1,10):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == str(num):
                tmp.append((i,j))

min_val = sys.maxsize

def getDist(a,b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2-x1) + abs(y2-y1)

def calc():
    dist = getDist(s, ans[0])
    dist += getDist(ans[0], ans[1])
    dist += getDist(ans[1], ans[2])
    dist += getDist(ans[2], e)
    return dist

ans = []
def choose(idx, cnt):
    global min_val

    if cnt == 3:
        min_val = min(min_val, calc())
        return

    if idx == len(tmp):
        return
    
    ans.append(tmp[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)
    
    
choose(0,0)

if min_val == sys.maxsize:
    min_val = -1

print(min_val)