n,m = map(int,input().split())

a = [
    input()
    for _ in range(n)
]

b = [
    input()
    for _ in range(n)
]

s = set()

def test(x,y,z):
    s.clear()

    for i in range(n):
        s.add(a[i][x:x+1] + a[i][y:y+1] + a[i][z:z+1])

    for i in range(n):
        if b[i][x:x+1] + b[i][y:y+1] + b[i][z:z+1] in s:
            return False
    return True

ans = 0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            if test(i,j,k):
                ans += 1
print(ans)