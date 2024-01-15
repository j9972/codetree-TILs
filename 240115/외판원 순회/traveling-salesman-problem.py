import sys
n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = []
min_val = sys.maxsize

def choose(addup, cnt = 0):
    global min_val

    if cnt == n:
        if arr[ans[-1]][ans[0]] == 0:
            return
        min_val = min(min_val, addup + arr[ans[-1]][ans[0]])
        return
    
    for i in range(n):
        if i in ans:
            continue

        if len(ans) > 0  and arr[ans[-1]][i] == 0:
            continue

        ans.append(i) # y값

        if len(ans) > 1:
            addup += arr[ans[-2]][ans[-1]]

        choose(addup, cnt+1)

        if len(ans) > 1:
            addup -= arr[ans[-2]][ans[-1]]

        ans.pop()

choose(0)
print(min_val)