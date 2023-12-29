n = int(input())

segments = []
for i in range(n):
    x,y = map(int,input().split())
    segments.append((x,y))

ans = 1000001
segments.sort()

for i in range(n):
    for j in range(i + 1, n):
        x1,y1 = segments[i]
        x2,y2 = segments[j]

        dist = abs(x2-x1) ** 2 + abs(y2-y1) ** 2
        ans = min(ans, dist)

print(ans)