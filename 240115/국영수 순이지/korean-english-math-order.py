n = int(input())

info = []
for i in range(n):
    name, k,e,m = input().split()
    info.append((name, int(k), int(e), int(m)))

info.sort(key = lambda x : (-x[1],-x[2],-x[3]))

for i in info:
    print(i[0], i[1], i[2],i[3])