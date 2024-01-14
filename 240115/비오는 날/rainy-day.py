class User:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

info = []
for i in range(n):
    date, day, weather = input().split()
    info.append(User(date, day, weather))

tmp = []
for i in range(n):
    tmp.append((info[i].date,info[i].day,info[i].weather))
tmp.sort()

for i in range(n):
    if tmp[i][2] == 'Rain':
        print(tmp[i][0],tmp[i][1],tmp[i][2])
        break