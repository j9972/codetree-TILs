from collections import defaultdict
n,k = map(int,input().split())

times = [
    tuple(map(int,input().split()))
    for _ in range(k)
]

arr = [0] + [i for i in range(1,n+1)]

#dic = {i: 1 for i in range(1, n+1)}
dic = {i: {i} for i in range(1, n+1)}

idx = 0
for i in range(1,3*k+1):
    idx1, idx2 = times[idx]

    #print("arr[idx1] : {}, arr[idx2] : {}".format(arr[idx1],arr[idx2]))

    dic[arr[idx1]].add(idx2)
    dic[arr[idx2]].add(idx1)
    #print("dic : {}", dic)

    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    #print("arr : {}".format(arr))
    idx += 1
    if i % k == 0:
        idx = 0
    #print('------------------------------')

for v in dic.values():
    print(len(v))