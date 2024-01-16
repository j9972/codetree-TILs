n,m = map(int,input().split())

arr = list(map(int,input().split()))

ans = []
visited = [False] * (n+1)

def choose(cur, idx):
    res = 0
    if cur == m+1:
        res = ans[0]
        for i in range(1,m):
            res = res ^ ans[i]
        return res

    max_val = 0
    for i in range(idx+1, n):
        ans.append(arr[i])
        max_val = max(max_val, choose(cur+1, i))
        ans.pop()
    return max_val
    # for i in range(n):
    #     if not visited[i]:
    #         visited[i] = True
    #         ans.append(arr[i])
            
    #         max_val = max(max_val, choose(cur+1))
            
    #         ans.pop()
    #         visited[i] = False

print(choose(1,-1))