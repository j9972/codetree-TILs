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

def choose(idx_num, cnt):
    global min_val

    if idx_num == n:
        if cnt == m:
            for i in range(m):
                for j in range(i+1,m):
                    min_val = min(min_val, getDist(arr[i], arr[j]))
        return
    
    ans.append(idx_num)
    choose(idx_num+1,cnt+1)
    ans.pop()
    choose(idx_num+1, cnt)

choose(0,0)
print(min_val)