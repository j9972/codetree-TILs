n = int(input())

segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def check(i,j,k):
    count = [0] * 101 # initialize
    over = False
    
    for a in range(n):
        if a in [i,j,k]:
            continue

        x1, x2 = segments[a]
        for b in range(x1, x2 + 1):
            count[b] += 1
    
    for a in range(101):
        if count[a] > 1:
            return False
    
    return True

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check(i,j,k):
                ans += 1


print(ans)