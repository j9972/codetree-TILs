n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
for i in range(n):
    over = False
    for j in range(n):

        if i == j:
            continue
        
        x1,x2 = arr[i]
        x3,x4 = arr[j]

        if (x1 <= x3 and x2 >= x4) or (x1 >= x3 and x2 <= x4):
            over = True
            break

    if not over:
        max_val += 1
        

print(max_val)