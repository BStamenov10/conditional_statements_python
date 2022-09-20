import math

world_record = float(input())
distance = float(input())
time_per_one_metre = float(input())

time_without_delay = distance * time_per_one_metre
delay_times = math.floor(distance / 15)
delay = delay_times * 12.5

all_time = time_without_delay + delay
diff = abs(world_record - all_time)
if world_record <= all_time:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
