import sys

n = int(input()) 
arr = list(input())

max_dist = 0
cur_i,cur_j = -1,-1

for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1' and arr[j] =='1':
            if max_dist < j - i:
                max_dist = j - i
                cur_i, cur_j = i,j
            break

max_dist2 , max_idx = -1,-1

if arr[0] == '0':
    dist = 0
    for i in range(1,n):
        if arr[i] == '1':
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        max_idx = 0

if arr[-1] == '0':
    dist = 0
    for i in range(n-2,-1,-1):
        if arr[i] == '1':
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        max_idx = n-1

if max_dist2 >= max_dist // 2:
    arr[max_idx] = '1'
else:
    arr[(cur_i + cur_j) // 2] = '1'


ans = sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1' and arr[j] =='1':
            ans = min(ans, j-i)
            break
print(ans)