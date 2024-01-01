m1, d1, m2, d2 = map(int,input().split())
a = input()

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]
    total_days += d
    
    return total_days    

diff = num_of_days(m2, d2) - num_of_days(m1, d1)

cnt = diff // 7
c = diff%7
gap = day_of_week.index(a) - 0

if gap <= c:
    cnt += 1
print(cnt)