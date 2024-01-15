info = list()
for i in range(5):
    name, h, w = input().split()
    info.append((name, int(h), w))

info.sort(key = lambda x : (x[0]))
print("name")
for i in info:
    print(i[0], i[1],i[2])

print()
info.sort(key = lambda x : -(x[1]))
print("height")
for i in info:
    print(i[0], i[1],i[2])