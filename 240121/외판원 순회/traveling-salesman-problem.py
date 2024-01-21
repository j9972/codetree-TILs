import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
visited = [False] * n
ans = []

def choose(cur_idx):
    global min_val

    if cur_idx == n:
        tot = 0
        for i in range(n-1):
            cost = arr[ans[i]][ans[i+1]]

            if cost == 0:
                return
            tot += cost
        
        addition = arr[ans[-1]][0]
        if addition == 0:
            return
        
        min_val = min(min_val, tot + addition)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(cur_idx + 1)

            ans.pop()
            visited[i] = False

visited[0] = True
ans.append(0)
choose(1)


print(min_val)