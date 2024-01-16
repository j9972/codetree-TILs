import sys
from itertools import combinations as cb
n,m = map(int,input().split())

min_val = sys.maxsize

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def find_dist(a,b,c,d):
    return (abs(c-a) ** 2) + (abs(d-b) ** 2)

possibleCB = list(cb(arr,m))

for possible in possibleCB:
    max_val = -sys.maxsize
    two = list(cb(possible,2))

    for i in two:
        distance = find_dist(i[0][0], i[0][1] , i[1][0], i[1][1])
        max_val = max(max_val, distance)

    min_val = min(max_val, min_val)

print(min_val)