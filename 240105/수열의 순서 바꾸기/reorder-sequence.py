n = int(input())
arr = list(map(int,input().split()))

# 최대 n-2
idx = n 
for i in range(n-2,-1,-1):
    if arr[i+1] < arr[i]:
        idx -= 1
    else:
        break
print(idx)