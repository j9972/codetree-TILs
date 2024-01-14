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


idx = 0
for i in range(n):
    if info[i].weather == 'Rain':
        idx = i
        break

print(info[idx].date,info[idx].day,info[idx].weather)