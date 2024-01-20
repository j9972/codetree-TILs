n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

minus, plus = 0,0

for a,b in arr:
    if a == b:
        continue
    if a > b:
        plus += 1
    else:
        minus += 1
print(max(plus, minus))