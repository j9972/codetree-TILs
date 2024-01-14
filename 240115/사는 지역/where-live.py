class User:
    def __init__(self, name, code,area):
        self.name = name
        self.code = code
        self.area = area

n = int(input())

info = []
for i in range(n):
    name, code, area = input().split()
    info.append(User(name, code, area))


tmp = []
for i in range(n):
    tmp.append((info[i].name, i))
tmp.sort()
idx = tmp[n-1][1]

print("name {}".format(info[idx].name))
print("addr {}".format(info[idx].code))
print("city {}".format(info[idx].area))