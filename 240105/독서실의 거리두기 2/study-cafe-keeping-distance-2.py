import sys

n = int(input())
seat = list(input())

max_dist = 0
mx, my = -1,-1

for i in range(n):
    if seat[i] == '1':
        for j in range(i+1,n):
            if seat[j] == '1':
                if j - i > max_dist:
                    max_dist = j - i

                    mx,my = i,j
                break

# 독서실 거리두기3과 다른 점은 양 끝이 1이 아니라 0일 수 있다는 점이다
max_dist2 = 0
idx = -1
if seat[0] == '0':
    dist = 0
    for i in range(1,n):
        if seat[i] == '1':
            break
        dist += 1
    if dist > max_dist2:
        max_dist2 = dist
        idx = 0

if seat[n-1] == '0':
    dist = 0
    for i in range(n-2,-1,-1):
        if seat[i] == '1':
            break
        dist += 1
    if dist > max_dist2:
        max_dist2 = dist
        idx = n-1

if max_dist // 2 >= max_dist2: 
    seat[(mx+my)//2] = '1'
else:
    seat[idx] = '1'

gap = sys.maxsize
for i in range(n):
    if seat[i] == '1':
        for j in range(i+1,n):
            if seat[j] == '1':
                gap = min(gap, j-i)
print(gap)