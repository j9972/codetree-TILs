import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
visited = [False] * (n+1)
ans = []

def choose(cur_idx):
    global min_val

    if cur_idx == n:
        min_val = min(min_val, sum(ans))
        return
    
    for i in range(n):

        if arr[cur_idx][i] == 0:
            continue

        if not visited[i]:
            visited[i] = True
            ans.append(arr[cur_idx][i])

            choose(cur_idx + 1)

            ans.pop()
            visited[i] = False
choose(0)
print(min_val)