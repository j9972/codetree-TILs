n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def count(i, j, h, g):
    c = 0
    for k in range(i, h + 1):
        for l in range(j, g + 1):
            c += 1
    return c

def check_all_positive(i, j, h, g):
    for k in range(i, h + 1):
        for l in range(j, g + 1):
            if arr[k][l] <= 0:
                return False
    return True

result = -1001

for i in range(n):
    for j in range(m):
        for i_ in range(n):
            for j_ in range(m):
                if check_all_positive(i, j, i_, j_):
                    result = max(
                        result, count(i, j, i_, j_)
                    )
if result == -1001:
    print(-1)
else:
    print(result)