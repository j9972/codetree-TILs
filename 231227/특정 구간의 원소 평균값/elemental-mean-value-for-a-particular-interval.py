n = int(input())
arr = list(map(int,input().split()))

ans = 0
max_sum = 0

for i in range(n):
    for j in range(i, n):
        sum_val = 0
        cnt = j - i + 1

        for k in range(i, j + 1):
            sum_val += arr[k]
        
        avg = sum_val / cnt

        for k in range(i, j + 1):
            if avg == arr[k]:
                ans += 1
                break
                

print(ans)