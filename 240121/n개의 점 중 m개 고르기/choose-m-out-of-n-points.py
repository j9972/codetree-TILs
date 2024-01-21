import sys

n,m = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def getDist(a,b):
    x1,y1 = a
    x2,y2 = b
    return (x1-x2)**2 + (y1-y2) ** 2

def calc():
    max_val = -sys.maxsize
    for i,val in enumerate(ans):
        for j,val2 in enumerate(ans):
            if i!=j:
                max_val = max(max_val, getDist(val,val2))
    return max_val

min_val = sys.maxsize
ans = []

def choose(idx,cnt):
    global min_val

    if cnt == m:
        min_val = min(min_val, calc())
        return
        
    if idx == n:
        return
    
    ans.append(arr[idx])
    choose(idx+1,cnt+1)
    ans.pop()
    choose(idx+1,cnt)

choose(0,0)
print(min_val)