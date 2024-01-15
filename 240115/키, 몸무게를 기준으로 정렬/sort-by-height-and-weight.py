n = int(input())
info = list()
for i in range(n):
    name, h, w = input().split()
    info.append((name, int(h), int(w)))


info.sort(key = lambda x : (x[1], -x[2]))
for i in info:
    print(i[0], i[1],i[2])