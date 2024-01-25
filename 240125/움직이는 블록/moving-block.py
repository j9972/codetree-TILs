n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

arr.sort()

mid = sum(arr)//n

gap = 0
for i in arr:
    if mid - i > 0:
        gap += mid-i
    else:
        break
print(gap)