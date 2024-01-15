import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = []
min_val = sys.maxsize
visited = [False] * n

def choose(cnt):
    global min_val

    if cnt == n:
        total = 0
        for i in range(n-1):
            sum_val = arr[ans[i]][ans[i+1]]
        
            if sum_val == 0:
                return
            total += sum_val

        
        addition = arr[ans[-1]][0] # 1번으로 돌아감
        if addition == 0:
            return

        min_val = min(min_val, total + addition)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(cnt+ 1)

            visited[i] = False
            ans.pop()


visited[0] = True
ans.append(0)
choose(1)
print(min_val)