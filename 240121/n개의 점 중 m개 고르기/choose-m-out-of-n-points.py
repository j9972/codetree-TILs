import sys
n,m = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = []
visited = [False]* (n+1)
min_val = sys.maxsize

def getDist(a,b):
    x1,y1 = a
    x2,y2 = b

    return (x1-x2) ** 2 + (y1-y2) ** 2

def Print():
    max_val = -sys.maxsize
    for i,val in enumerate(ans):
        distance = 0
        for j,val2 in enumerate(ans):
            if i == j:
                continue
            distance = getDist(val, val2)
            max_val = max(max_val, distance)
    return max_val

def choose(idx_num, cnt):
    global min_val

    if cnt == m:
        min_val = min(min_val, Print())
        return

    if idx_num == n:
        return
    
    ans.append(arr[idx_num])
    choose(idx_num+1,cnt+1)
    ans.pop()
    choose(idx_num+1, cnt)

choose(0,0)
print(min_val)