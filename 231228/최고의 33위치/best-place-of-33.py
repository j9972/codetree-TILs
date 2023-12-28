n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_value = 0
for i in range(n-2):
    for j in range(n-2):
        sum_value = 0
        for k in range(i,i+3):
            for h in range(j,j+3):
                sum_value += arr[k][h]
        max_value = max(max_value, sum_value)
print(max_value)