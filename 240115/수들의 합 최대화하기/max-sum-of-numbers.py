n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False] * (n+1)
ans = []
max_val = 0

def choose(row):
    global max_val

    if row == n:
        sum_val = 0
        for i in range(n):
            sum_val += arr[i][ans[i]]
        
        max_val = max(max_val, sum_val)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(row+1)

            ans.pop()
            visited[i] = False
choose(0)
print(max_val)