n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

one, two = 0,0

for a,b in arr:
    if a == b:
        continue
    if abs(a-b) == 1:
        one += 1
    else:
        two += 1
print(max(one, two))