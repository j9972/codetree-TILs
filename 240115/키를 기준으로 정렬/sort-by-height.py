n = int(input())

info = []
for i in range(n):
    name, h,w = input().split()
    info.append((name, int(h), int(w)))

info.sort(key = lambda x : x[1])

for i in info:
    print(i[0], i[1], i[2])