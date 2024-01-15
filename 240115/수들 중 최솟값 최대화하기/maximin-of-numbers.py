import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False] * (n+1)
ans = []
res = []

def choose(row):

    if row == n:
        tmp = []
        for i in range(n):
            tmp.append(arr[i][ans[i]])
        res.append(min(tmp))
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(row+1)

            ans.pop()
            visited[i] = False
choose(0)
print(max(res))