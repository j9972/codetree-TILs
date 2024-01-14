n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

d = [0] * 1001
cnt = 0

for i in arr:
    x1,x2 = i
    flag = False
    
    for j in range(x1,x2+1):
        if d[j] == 1:
            flag = True
            break
        d[j] = 1

    if flag == False:
        cnt += 1
print(cnt)