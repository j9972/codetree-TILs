n = int(input())
arr = list(map(int,input().split()))

cnt = n - 1
for i in range(n-2,-1,-1):
    if arr[i+1] > arr[i]:
        cnt -= 1
    else:
        break
print(cnt)