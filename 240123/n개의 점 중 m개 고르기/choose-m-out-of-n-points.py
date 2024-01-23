import sys

n,m = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def getDist(a,b):
    x1,y1 = a
    x2,y2 = b
    return (x2-x1) ** 2 + (y2-y1) ** 2

min_val = sys.maxsize
ans = list()

def choose(idx):
    global min_val

    if idx == m:
        for i, val in enumerate(ans):
            for j, val1 in enumerate(ans):
                if i != j:
                    min_val = min(min_val, getDist(val1, val))
        return 

    
    # if idx == n:
    #     return
    
    ans.append(arr[idx])
    choose(idx+1)
    #choose(idx+1, cnt+1)
    ans.pop()
    #choose(idx+1, cnt)

choose(0)
print(min_val)