n , m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_value = 0

# 1 * 2 -> 2 * 2 에서 최소값 하나 뺴기
def square(x,y):
    sum_value = arr[x][y]+arr[x+1][y]+arr[x][y+1]+arr[x+1][y+1]
    min_value = min(arr[x][y],arr[x+1][y],arr[x][y+1],arr[x+1][y+1])
    return sum_value - min_value

for i in range(n-1):
    for j in range(m-1):
        max_value = max(max_value, square(i,j))

# 1 * 3
def longSquare(x,y):
    return arr[x][y] + arr[x][y+1] +arr[x][y+2]
def colLongSquare(x,y):
    return arr[x][y] + arr[x+1][y] +arr[x+2][y]

for i in range(n):
    for j in range(m-2):
        max_value = max(max_value, longSquare(i,j))

for j in range(m):
    for i in range(n-2):
        max_value = max(max_value, colLongSquare(i,j))
print(max_value)