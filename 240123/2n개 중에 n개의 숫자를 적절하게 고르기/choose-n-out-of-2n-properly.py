import sys

n = int(input())
arr = list(map(int,input().split()))

min_val = sys.maxsize
ans = list()

def choose(idx,cnt):
    global min_val

    if cnt == n:
        min_val = min(min_val, abs(sum(arr) - sum(ans) * 2))

    if idx == 2*n:
        return

    ans.append(arr[idx])
    choose(idx + 1 , cnt + 1)
    ans.pop()
    choose(idx + 1 , cnt)

choose(0,0)
print(min_val)