n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
max_val = 0
for i in range(n):
    d = [0] * (1001)
    for j in range(i+1,n):

        x,y = arr[j]

        for time in range(x,y):
            d[time] += 1
        
    max_val = max(max_val,sum(d))
print(max_val)