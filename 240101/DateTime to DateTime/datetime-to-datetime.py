d,h,m = map(int,input().split())

if d == 11 and (h < 11 or (h >= 11 and m < 11)):
    print(-1)
else:
    time = 1440 - (671)

    if d == 11:
        print(time) 
    else:
        time += (d-12)*24*60+(h*60+m)
        print(time)