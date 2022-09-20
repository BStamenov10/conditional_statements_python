init_hour = int(input())
init_minutes = int(input())

total_time_min = (init_hour * 60) + init_minutes + 15
total_hour = total_time_min // 60
total_min = total_time_min % 60

if total_hour > 23:
    total_hour = 0

if total_min < 10:
    print(f"{total_hour}:0{total_min}")
else:
    print(f"{total_hour}:{total_min}")
