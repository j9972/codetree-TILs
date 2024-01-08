n,m = map(int,input().split())

arr = [
    input()
    for _ in range(n)
]
target = [
    input()
    for _ in range(m)
]

for i in range(m):
    if target[i].isdigit():
        print(arr[int(target[i])-1])
    else:
        print(arr.index(target[i])+1)