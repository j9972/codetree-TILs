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

seat[(maxX+maxY) // 2] = '1'
gap = sys.maxsize

for i in range(n):
    if int(seat[i]) == 1:
        for j in range(i+1,n):
            if int(seat[j]) == 1:
                gap = min(gap, abs(j-i))
print(gap)