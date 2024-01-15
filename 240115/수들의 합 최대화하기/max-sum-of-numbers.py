n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False] * (n+1)
max_val = -1

def choose(cnt, sum_val):
    global max_val

    if cnt == n:
        max_val = max(max_val, sum_val)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            choose(cnt+1, sum_val + arr[cnt][i])
            visited[i] = False

choose(0,0)       
print(max_val)