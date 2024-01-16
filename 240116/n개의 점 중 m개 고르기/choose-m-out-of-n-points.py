import sys
n,m = map(int,input().split())

arr =[
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = []
min_val = sys.maxsize

def find_dist(a,b,c,d):
    return (c-a) ** 2 + (d-b) ** 2

def choose(idx, cnt):
    global min_val    
    if cnt == m:
        for i, val1 in enumerate(ans):
            for j, val2 in enumerate(ans):
                if i != j:
                    min_val = min(min_val, find_dist(val1[0], val1[1], val2[0], val2[1]))
                    return
    if idx == n:
        return

    ans.append(arr[idx])
    choose(idx+1,cnt+1)
    ans.pop()

    choose(idx+1, cnt)

choose(0,0)
print(min_val)