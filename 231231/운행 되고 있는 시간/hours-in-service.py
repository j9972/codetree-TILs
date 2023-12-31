n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
for i in range(n): # 해고되는 개발자
    d = [0] * (1001)
    for j, (x,y) in enumerate(arr):
        if i == j:
            continue

        for time in range(x,y):
            d[time] = 1
    
    max_val = max(max_val,sum(d))
print(max_val)