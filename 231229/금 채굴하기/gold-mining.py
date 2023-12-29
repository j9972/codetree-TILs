n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cost_gold(x,y):
    # x,y 는 현재 지점
    mg = 0
    for dist in range(2 * (n - 1) + 1):
        gold = 0
        for i in range(n):
            for j in range(n):
                if abs(i-x) + abs(j-y) <= dist:
                    if arr[i][j] == 1:
                        gold += 1
        if gold * m >= dist ** 2 + (dist+1) ** 2:
            mg = max(mg, gold)
    return mg


max_gold = 0
for i in range(n):
    for j in range(n):
        max_gold = max(max_gold, cost_gold(i,j))
        
print(max_gold)