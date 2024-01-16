import sys

n = int(input())
arr = list(map(int,input().split()))

ans = []
total = sum(arr)
visited = [False] * (2 * n+1)

min_val = sys.maxsize

def choose(cnt):
    global min_val

    if cnt == n:
        min_val = min(min_val, abs((total - sum(ans)) - sum(ans)))
        return
    
    for i in range(2*n):
        if not visited[i]:
            ans.append(arr[i])
            visited[i] = True
            choose(cnt+1)
            ans.pop()
            visited[i] = False
choose(0)
print(min_val)