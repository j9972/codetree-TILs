import sys
n = int(input())

arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])

cnt = sys.maxsize

for i in range(n):
    minx,miny = sys.maxsize,sys.maxsize
    maxx,maxy = 1,1
    for j in range(n):
        if i == j:
            continue
        x,y = arr[j]
        minx = min(minx,x)
        miny = min(miny,y)
        maxx = max(maxx,x)
        maxy = max(maxy,y)

    cnt = min(cnt, (maxx - minx) * (maxy - miny))
print(cnt)