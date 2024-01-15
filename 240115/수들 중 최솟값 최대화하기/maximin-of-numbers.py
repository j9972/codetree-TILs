import sys
INT_MAX = sys.maxsize

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False] * n
ans = []
max_val = 0

def choose(row):
    global max_val

    if row == n:
        min_num = INT_MAX
        for i in range(n):
            min_num = min(min_num, arr[i][ans[i]])

        max_val = max(max_val, min_num)
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