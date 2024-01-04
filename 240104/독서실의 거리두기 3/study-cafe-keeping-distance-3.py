import sys

n = int(input())
seat = list(input())
gap = sys.maxsize
res = []

for i in range(n):
    if seat[i] == '0':
        # print(i)
        # seat[i] = '1'

        dist, dist2 = 0, 0

        for j in range(i-1,-1,-1):
            if seat[j] == '1':
                dist = abs(i-j)
                break
        for j in range(i+1,n):
            if seat[j] == '1':
                dist2 = abs(i-j)
                break

#        print(dist, dist2)
        res.append(min(dist, dist2))
    
        #seat[i] = 0
print(max(res))