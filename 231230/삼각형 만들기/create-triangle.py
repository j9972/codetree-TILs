n = int(input())
segments = []
OFFSET = 10000
for i in range(n):
    x,y = map(int,input().split())
    segments.append((x+10000,y+10000))

# 3중 2개가 x값이 같다.
segments.sort()
#print(segments)
ans = 0

for i in range(n):
    for j in range(i+1,n):
        if segments[i][0] == segments[j][0]:
            height = max(abs(segments[i][0] - segments[n-1][0]), abs(segments[i][0] - segments[0][0]))
            triangle = (segments[j][1] - segments[i][1]) * height
            ans = max(ans, triangle)
print(ans)