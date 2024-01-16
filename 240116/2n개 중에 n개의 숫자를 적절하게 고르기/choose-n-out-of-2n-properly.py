import sys

n = int(input())
arr = list(map(int,input().split()))

visited = [False] * (2 * n)

min_val = sys.maxsize

def calc():
    diff = 0
    for i in range(2*n):
        if visited[i]:
            diff += arr[i]
        else:
            diff -= arr[i]
    return abs(diff)

def choose(idx, cnt):
    global min_val

    if cnt == n:
        min_val = min(min_val, calc())
        return
    if idx == 2*n:
        return
    
    visited[idx] = True

    choose(idx+1,cnt+1)
    visited[idx] = False

    choose(idx+1, cnt)
choose(0,0)
print(min_val)
# import sys
# from itertools import combinations as cb

# n = int(input())
# arr = list(map(int,input().split()))

# tmp = list(cb(arr,n))

# min_val = sys.maxsize

# for i in tmp:
#     min_val = min(min_val, abs((sum(arr) - sum(i)) - sum(i)))
# print(min_val)