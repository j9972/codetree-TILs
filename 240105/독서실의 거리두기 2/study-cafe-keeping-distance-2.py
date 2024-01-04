import sys

n = int(input())
seat = list(input())

max_dist = 0
maxX, maxY = -1,-1

for i in range(n):
    if int(seat[i]) == 1:
        for j in range(i+1,n):
            if int(seat[j]) == 1:

                if j - i > max_dist:
                    max_dist = abs(j-i)

                    maxX,maxY = i,j
                break

max_dist2, max_idx = -1,-1
if seat[0] == '0':
    dist = 0
    for i in range(1,n):
        if seat[i] == '1':
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        max_idx = 0

if seat[n-1] == '0':
    dist = 0
    for i in range(n-2,-1,-1):
        if seat[i] == '1':
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        max_idx = n -1



if max_dist2 >= max_dist // 2:
    seats[max_idx] = '1'
else:
    seats[(max_i + max_j) // 2] = '1'
    
gap = sys.maxsize

for i in range(n):
    if int(seat[i]) == 1:
        for j in range(i+1,n):
            if int(seat[j]) == 1:
                gap = min(gap, abs(j-i))
print(gap)