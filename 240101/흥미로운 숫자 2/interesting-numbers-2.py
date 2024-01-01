x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):

    res = set()
    for j in str(i):
        res.add(j)
    
    if len(res) == 2:
        ans += 1
print(ans)