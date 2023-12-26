n = int(input())
cow = [0] + list(map(int,input().split()))

cnt = 0

for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            if cow[i] <= cow[j] <= cow[k]:
                cnt += 1
print(cnt)