n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
ans = []
visited = [False] * (n+1)

def choose(cur_idx, cur_cnt):
    global max_val

    if cur_cnt == n:
        #print(ans)
        total = 0
        for e in ans:
            total += e
        max_val = max(max_val, total)
        return
    
    if cur_idx == n:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[cur_idx][i])
        
            choose(cur_idx + 1, cur_cnt + 1)
            ans.pop()

            choose(cur_idx + 1, cur_cnt)
            visited[i] = False

choose(0,0)
print(max_val)