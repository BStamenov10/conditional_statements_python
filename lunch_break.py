import math

name_series = input()
episode_duration = int(input())
rest_duration = int(input())

time_for_lunch = rest_duration * 1/8
time_for_rest = rest_duration * 1/4
time_left = rest_duration - time_for_lunch - time_for_rest

diff = abs(time_left - episode_duration)
rounded_diff = math.ceil(diff)

if time_left >= episode_duration:
    print(f"You have enough time to watch {name_series} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {rounded_diff} more minutes.")