m1, d1, m2, d2 = map(int,input().split())

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

left_days = 0
for i in range(m1,m2):
    left_days += num_of_days[i] 

left_days -= d1
left_days += d2

if left_days % 7 == 0:
    print(day[0])
elif left_days % 7 == 1:
    print(day[1])
elif left_days % 7 == 2:
    print(day[2])
elif left_days % 7 == 3:
    print(day[3])
elif left_days % 7 == 4:
    print(day[4])
elif left_days % 7 == 5:
    print(day[5])
elif left_days % 7 == 6:
    print(day[6])