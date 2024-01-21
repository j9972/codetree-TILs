import sys

n = int(input())
arr = list(map(int,input().split()))

visited = [False] * (2*n)
ans = []
min_val = sys.maxsize

def choose(idx,cnt):
    global min_val
    
    if cnt == n:
        diff = 0
        for i in range(2*n):
            if visited[i]:
                diff += arr[i]
            else:
                diff -= arr[i]
        min_val = min(min_val, abs(diff))

    if idx == 2*n:
        return

    visited[idx] = True
    choose(idx+1, cnt+1)
    visited[idx] = False
    choose(idx+1, cnt)

choose(0,0)
print(min_val)