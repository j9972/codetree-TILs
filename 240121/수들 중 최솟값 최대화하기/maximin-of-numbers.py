import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
ans = []
visited = [False] * (n+1)

def choose(cur_idx):
    global max_val

    if cur_idx == n:
        max_val = max(max_val, min(ans))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[cur_idx][i])

            choose(cur_idx + 1)

            ans.pop()
            visited[i] = False
choose(0)
print(max_val)