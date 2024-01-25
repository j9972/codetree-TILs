import sys
n = int(input())
arr = [0] + list(map(int,input().split()))

min_val = sys.maxsize

arr.sort()

for i in range(1,n+1):
    min_val = min(min_val, arr[i+n] - arr[i])
print(min_val)