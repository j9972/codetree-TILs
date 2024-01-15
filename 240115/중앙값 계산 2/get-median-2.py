n = int(input())
arr = list(map(int,input().split()))

tmp = []
for i in range(n):
    tmp.append(arr[i])
    tmp.sort()
    if i % 2 == 0:
        print(tmp[i//2],end =' ')