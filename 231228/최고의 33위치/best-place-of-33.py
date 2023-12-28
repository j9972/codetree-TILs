n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_value = 0
for i in range(n-2):
    for j in range(n-2):
        sum_value = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 

        max_value = max(max_value, sum_value)
print(max_value)